# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
_logger = logging.getLogger(__name__)
import time
import pytz
from datetime import datetime,date, timedelta

from odoo import osv
from odoo import models, fields, api, _

from .grpcproto import odoo_pb2
from .grpcproto import weladee_pb2
from . import weladee_employee
from .sync.weladee_base import myrequest, sync_loginfo, sync_logerror, sync_logdebug, sync_logwarn, sync_stop, sync_has_error

from odoo.addons.Weladee_Attendances.models.weladee_settings import get_synchronous_email, get_synchronous_debug 
from odoo.addons.Weladee_Attendances.models.sync.weladee_position import sync_position_data, sync_position 
from odoo.addons.Weladee_Attendances.models.sync.weladee_department import sync_department_data, sync_department
from odoo.addons.Weladee_Attendances.models.sync.weladee_employee import sync_employee_data, sync_employee
from odoo.addons.Weladee_Attendances.models.sync.weladee_manager import sync_manager
from odoo.addons.Weladee_Attendances.models.sync.weladee_log import sync_log
from odoo.addons.Weladee_Attendances.models.sync.weladee_holiday import sync_holiday

class weladee_attendance_working(models.TransientModel):
      _name="weladee_attendance.working"  

      last_run = fields.Datetime('Last run')

class weladee_attendance(models.TransientModel):
    _name="weladee_attendance.synchronous"
    _description="synchronous Employee, Department, Holiday and attendance"

    @api.model
    def start_sync(self):
        '''
            request-date : date user request to sync
            request-error : if error and stop ?
            request-logs : logs info
            request-email : email recipient
            request-debug : display debug log
        '''
        elapse_start = datetime.today()
        user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz or 'UTC')
        today = elapse_start.astimezone(user_tz)
        context_sync = {
            'request-date':today.strftime('%d/%m/%Y %H:%M'),
            'request-logs':[],
            'request-error':False,
            'request-email':get_synchronous_email(self),
            'request-debug':get_synchronous_debug(self)
        }
        sync_loginfo(context_sync,"Starting sync..")
        authorization, holiday_status_id, api_db = weladee_employee.get_api_key(self)

        if api_db and (api_db != self.env.cr.dbname):
           sync_stop(context_sync)
           sync_logerror(context_sync,'Warning this api key of (%s) is not match with current database' % api_db)
        
        if (not holiday_status_id) or (not authorization) and (api_db == self.env.cr.dbname):
            #raise exceptions.UserError('Must to be set Leave Type on Weladee setting')
            sync_stop(context_sync)
            sync_logerror(context_sync,'You must setup API Key, Holiday Status at Attendances -> Weladee settings')
        
        if not sync_has_error(context_sync):
            sync_logdebug(context_sync,"Start sync...Positions")
            job_obj = self.env['hr.job']    
            sync_position(job_obj, authorization, context_sync) 

        if not sync_has_error(context_sync):
            sync_logdebug(context_sync,"Start sync...Departments")
            department_obj = self.env['hr.department']    
            sync_department(department_obj, authorization, context_sync)

            '''
            if not context_sync['request-error']:
               _logger.info("Loading...Countries")
               country = {}
               country_line_ids = self.env['res.country'].search([])
               for cu in country_line_ids:
                   if cu.name :
                      country[ cu.name.lower() ] = cu.id

            if not context_sync['request-error']:
               _logger.info("Start sync...Employee")
               return_managers = {}
               emp_obj = self.env['hr.employee']    
               sync_employee(job_obj, emp_obj, department_obj, country, authorization, return_managers, context_sync)

            if not context_sync['request-error']:
               _logger.info("Start sync...Manager")
               sync_manager(emp_obj, return_managers, authorization, context_sync)

            odoo_weladee_ids = {}
            if not context_sync['request-error']:
               _logger.info("Start sync...Log")
               att_obj = self.env['hr.attendance']
               sync_log(emp_obj, att_obj, authorization, context_sync, odoo_weladee_ids)

            if not context_sync['request-error']:
               _logger.info("Start sync...Holiday")
               hr_obj = self.env['hr.holidays']
               com_hr_obj = self.env['weladee_attendance.company.holidays']
               sync_holiday(emp_obj, hr_obj, com_hr_obj, authorization, context_sync, odoo_weladee_ids, holiday_status_id)
            '''

        sync_loginfo(context_sync,'sending result to %s' % context_sync['request-email'])
        self.send_result_mail(context_sync)
        works = self.env['weladee_attendance.working'].search([])
        if works: works.unlink()

    def send_result_mail(self, ctx):
        '''
        send result email to admin
        '''
        template = self.env.ref('Weladee_Attendances.weladee_attendance_synchronous_cron_mail', raise_if_not_found=False)
        
        if template:
           template.with_context(ctx).send_mail(self.id)        
        else:
           _logger.error('sending result to %s failed, no template found' % ctx['request-email'])            
