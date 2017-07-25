# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import weladee_pb2 as weladee__pb2


class MobileStub(object):
  """*
  List of available functions for mobile device.
  Don't forget to authenticate yourself with metadata "token" with token you got from signIn API function
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetEmployee = channel.unary_unary(
        '/grpc.weladee.com.Mobile/GetEmployee',
        request_serializer=weladee__pb2.EmployeeRequest.SerializeToString,
        response_deserializer=weladee__pb2.Employee.FromString,
        )
    self.GetEmployees = channel.unary_stream(
        '/grpc.weladee.com.Mobile/GetEmployees',
        request_serializer=weladee__pb2.EmployeesRequest.SerializeToString,
        response_deserializer=weladee__pb2.Employee.FromString,
        )
    self.GetHolidays = channel.unary_stream(
        '/grpc.weladee.com.Mobile/GetHolidays',
        request_serializer=weladee__pb2.EmployeeRequest.SerializeToString,
        response_deserializer=weladee__pb2.Holiday.FromString,
        )
    self.GetLogEvent = channel.unary_stream(
        '/grpc.weladee.com.Mobile/GetLogEvent',
        request_serializer=weladee__pb2.Empty.SerializeToString,
        response_deserializer=weladee__pb2.LogEvent.FromString,
        )


class MobileServicer(object):
  """*
  List of available functions for mobile device.
  Don't forget to authenticate yourself with metadata "token" with token you got from signIn API function
  """

  def GetEmployee(self, request, context):
    """/ return employee record based on id, email or user_name
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEmployees(self, request, context):
    """/ Stream of employees
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetHolidays(self, request, context):
    """/ Stream of active holidays of an employee including company holidays
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLogEvent(self, request, context):
    """*
    Realtime event when employee check in/out.
    Get a stream for each in/out in the company depending on token or authorization.
    It can be limited to an employee, a team or entire company.
    The header contains "employees": an array of all employeeid who are IN at the moment the request was done.
    Header example : "employees":["6762","451","152"]
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MobileServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetEmployee': grpc.unary_unary_rpc_method_handler(
          servicer.GetEmployee,
          request_deserializer=weladee__pb2.EmployeeRequest.FromString,
          response_serializer=weladee__pb2.Employee.SerializeToString,
      ),
      'GetEmployees': grpc.unary_stream_rpc_method_handler(
          servicer.GetEmployees,
          request_deserializer=weladee__pb2.EmployeesRequest.FromString,
          response_serializer=weladee__pb2.Employee.SerializeToString,
      ),
      'GetHolidays': grpc.unary_stream_rpc_method_handler(
          servicer.GetHolidays,
          request_deserializer=weladee__pb2.EmployeeRequest.FromString,
          response_serializer=weladee__pb2.Holiday.SerializeToString,
      ),
      'GetLogEvent': grpc.unary_stream_rpc_method_handler(
          servicer.GetLogEvent,
          request_deserializer=weladee__pb2.Empty.FromString,
          response_serializer=weladee__pb2.LogEvent.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.weladee.com.Mobile', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class OdooStub(object):
  """*
  List of available functions for Odoo only.
  Don't forget to authenticate yourself with metadata "authorization" with api_key
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetEmployee = channel.unary_unary(
        '/grpc.weladee.com.Odoo/GetEmployee',
        request_serializer=weladee__pb2.OdooRequest.SerializeToString,
        response_deserializer=weladee__pb2.EmployeeOdoo.FromString,
        )
    self.UpdateEmployee = channel.unary_unary(
        '/grpc.weladee.com.Odoo/UpdateEmployee',
        request_serializer=weladee__pb2.EmployeeOdoo.SerializeToString,
        response_deserializer=weladee__pb2.Empty.FromString,
        )
    self.GetEmployees = channel.unary_stream(
        '/grpc.weladee.com.Odoo/GetEmployees',
        request_serializer=weladee__pb2.Empty.SerializeToString,
        response_deserializer=weladee__pb2.EmployeeOdoo.FromString,
        )
    self.AddEmployee = channel.unary_unary(
        '/grpc.weladee.com.Odoo/AddEmployee',
        request_serializer=weladee__pb2.EmployeeOdoo.SerializeToString,
        response_deserializer=weladee__pb2.AddResult.FromString,
        )
    self.GetHolidays = channel.unary_stream(
        '/grpc.weladee.com.Odoo/GetHolidays',
        request_serializer=weladee__pb2.OdooRequest.SerializeToString,
        response_deserializer=weladee__pb2.HolidayOdoo.FromString,
        )
    self.GetCompanyHolidays = channel.unary_stream(
        '/grpc.weladee.com.Odoo/GetCompanyHolidays',
        request_serializer=weladee__pb2.Empty.SerializeToString,
        response_deserializer=weladee__pb2.HolidayOdoo.FromString,
        )
    self.AddHoliday = channel.unary_unary(
        '/grpc.weladee.com.Odoo/AddHoliday',
        request_serializer=weladee__pb2.HolidayOdoo.SerializeToString,
        response_deserializer=weladee__pb2.AddResult.FromString,
        )
    self.DropHoliday = channel.unary_unary(
        '/grpc.weladee.com.Odoo/DropHoliday',
        request_serializer=weladee__pb2.OdooRequest.SerializeToString,
        response_deserializer=weladee__pb2.Empty.FromString,
        )
    self.UpdateHoliday = channel.unary_unary(
        '/grpc.weladee.com.Odoo/UpdateHoliday',
        request_serializer=weladee__pb2.HolidayOdoo.SerializeToString,
        response_deserializer=weladee__pb2.Empty.FromString,
        )
    self.GetDepartment = channel.unary_unary(
        '/grpc.weladee.com.Odoo/GetDepartment',
        request_serializer=weladee__pb2.OdooRequest.SerializeToString,
        response_deserializer=weladee__pb2.DepartmentOdoo.FromString,
        )
    self.GetDepartments = channel.unary_stream(
        '/grpc.weladee.com.Odoo/GetDepartments',
        request_serializer=weladee__pb2.Empty.SerializeToString,
        response_deserializer=weladee__pb2.DepartmentOdoo.FromString,
        )
    self.AddDepartment = channel.unary_unary(
        '/grpc.weladee.com.Odoo/AddDepartment',
        request_serializer=weladee__pb2.DepartmentOdoo.SerializeToString,
        response_deserializer=weladee__pb2.AddResult.FromString,
        )
    self.UpdateDepartment = channel.unary_unary(
        '/grpc.weladee.com.Odoo/UpdateDepartment',
        request_serializer=weladee__pb2.DepartmentOdoo.SerializeToString,
        response_deserializer=weladee__pb2.Empty.FromString,
        )
    self.GetNewAttendance = channel.unary_stream(
        '/grpc.weladee.com.Odoo/GetNewAttendance',
        request_serializer=weladee__pb2.Empty.SerializeToString,
        response_deserializer=weladee__pb2.LogEventOdoo.FromString,
        )
    self.SyncAttendance = channel.stream_unary(
        '/grpc.weladee.com.Odoo/SyncAttendance',
        request_serializer=weladee__pb2.LogEventOdooSync.SerializeToString,
        response_deserializer=weladee__pb2.Empty.FromString,
        )
    self.GetPositions = channel.unary_stream(
        '/grpc.weladee.com.Odoo/GetPositions',
        request_serializer=weladee__pb2.Empty.SerializeToString,
        response_deserializer=weladee__pb2.PositionOdoo.FromString,
        )
    self.AddPosition = channel.unary_unary(
        '/grpc.weladee.com.Odoo/AddPosition',
        request_serializer=weladee__pb2.PositionOdoo.SerializeToString,
        response_deserializer=weladee__pb2.AddResult.FromString,
        )


class OdooServicer(object):
  """*
  List of available functions for Odoo only.
  Don't forget to authenticate yourself with metadata "authorization" with api_key
  """

  def GetEmployee(self, request, context):
    """/ Employee
    / return employee record based on id, odoo_id, email or user_name
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateEmployee(self, request, context):
    """*
    updates the Employee from odoo in the database.
    Only few fields can be updated:
    phones, first_name_english, last_name_english, email, nickname_english,
    last_name_thai, active, code, first_name_thai, nickname_thai
    positionid, photo.
    Raise error if fails
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEmployees(self, request, context):
    """/ Stream of employees
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddEmployee(self, request, context):
    """/ Add employee, get the id as return.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetHolidays(self, request, context):
    """/ Holiday
    / Stream of holidays for 1 employee
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCompanyHolidays(self, request, context):
    """/ Stream of holidays for the company
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddHoliday(self, request, context):
    """/ Add holiday, get the id as return.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DropHoliday(self, request, context):
    """/ Remove holiday from database
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateHoliday(self, request, context):
    """/ Update holiday. raise error if fails
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDepartment(self, request, context):
    """/ Department
    / return department record based on id or odoo_id
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDepartments(self, request, context):
    """/ return a stream of departments
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddDepartment(self, request, context):
    """/ Add department, get the id as return.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateDepartment(self, request, context):
    """/ Update a department. raise error if fails
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNewAttendance(self, request, context):
    """/ Attendance
    / return a stream of attendance record + odoo employee id that have not yet been synchronized with Odoo or that need to be synchronized again.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SyncAttendance(self, request_iterator, context):
    """/ Send a stream of LogEventSync to confirm the log entries have been synchronized with Odoo. This funciton use a stream in order to synchronize a large bunch of records very quickly. Odoo can not update or create or delete LogEvent record in Weladee.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPositions(self, request, context):
    """/ Position
    / return a stream of positions. Called "job title" in odoo
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddPosition(self, request, context):
    """/ Add position, get the id as return.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OdooServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetEmployee': grpc.unary_unary_rpc_method_handler(
          servicer.GetEmployee,
          request_deserializer=weladee__pb2.OdooRequest.FromString,
          response_serializer=weladee__pb2.EmployeeOdoo.SerializeToString,
      ),
      'UpdateEmployee': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateEmployee,
          request_deserializer=weladee__pb2.EmployeeOdoo.FromString,
          response_serializer=weladee__pb2.Empty.SerializeToString,
      ),
      'GetEmployees': grpc.unary_stream_rpc_method_handler(
          servicer.GetEmployees,
          request_deserializer=weladee__pb2.Empty.FromString,
          response_serializer=weladee__pb2.EmployeeOdoo.SerializeToString,
      ),
      'AddEmployee': grpc.unary_unary_rpc_method_handler(
          servicer.AddEmployee,
          request_deserializer=weladee__pb2.EmployeeOdoo.FromString,
          response_serializer=weladee__pb2.AddResult.SerializeToString,
      ),
      'GetHolidays': grpc.unary_stream_rpc_method_handler(
          servicer.GetHolidays,
          request_deserializer=weladee__pb2.OdooRequest.FromString,
          response_serializer=weladee__pb2.HolidayOdoo.SerializeToString,
      ),
      'GetCompanyHolidays': grpc.unary_stream_rpc_method_handler(
          servicer.GetCompanyHolidays,
          request_deserializer=weladee__pb2.Empty.FromString,
          response_serializer=weladee__pb2.HolidayOdoo.SerializeToString,
      ),
      'AddHoliday': grpc.unary_unary_rpc_method_handler(
          servicer.AddHoliday,
          request_deserializer=weladee__pb2.HolidayOdoo.FromString,
          response_serializer=weladee__pb2.AddResult.SerializeToString,
      ),
      'DropHoliday': grpc.unary_unary_rpc_method_handler(
          servicer.DropHoliday,
          request_deserializer=weladee__pb2.OdooRequest.FromString,
          response_serializer=weladee__pb2.Empty.SerializeToString,
      ),
      'UpdateHoliday': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateHoliday,
          request_deserializer=weladee__pb2.HolidayOdoo.FromString,
          response_serializer=weladee__pb2.Empty.SerializeToString,
      ),
      'GetDepartment': grpc.unary_unary_rpc_method_handler(
          servicer.GetDepartment,
          request_deserializer=weladee__pb2.OdooRequest.FromString,
          response_serializer=weladee__pb2.DepartmentOdoo.SerializeToString,
      ),
      'GetDepartments': grpc.unary_stream_rpc_method_handler(
          servicer.GetDepartments,
          request_deserializer=weladee__pb2.Empty.FromString,
          response_serializer=weladee__pb2.DepartmentOdoo.SerializeToString,
      ),
      'AddDepartment': grpc.unary_unary_rpc_method_handler(
          servicer.AddDepartment,
          request_deserializer=weladee__pb2.DepartmentOdoo.FromString,
          response_serializer=weladee__pb2.AddResult.SerializeToString,
      ),
      'UpdateDepartment': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateDepartment,
          request_deserializer=weladee__pb2.DepartmentOdoo.FromString,
          response_serializer=weladee__pb2.Empty.SerializeToString,
      ),
      'GetNewAttendance': grpc.unary_stream_rpc_method_handler(
          servicer.GetNewAttendance,
          request_deserializer=weladee__pb2.Empty.FromString,
          response_serializer=weladee__pb2.LogEventOdoo.SerializeToString,
      ),
      'SyncAttendance': grpc.stream_unary_rpc_method_handler(
          servicer.SyncAttendance,
          request_deserializer=weladee__pb2.LogEventOdooSync.FromString,
          response_serializer=weladee__pb2.Empty.SerializeToString,
      ),
      'GetPositions': grpc.unary_stream_rpc_method_handler(
          servicer.GetPositions,
          request_deserializer=weladee__pb2.Empty.FromString,
          response_serializer=weladee__pb2.PositionOdoo.SerializeToString,
      ),
      'AddPosition': grpc.unary_unary_rpc_method_handler(
          servicer.AddPosition,
          request_deserializer=weladee__pb2.PositionOdoo.FromString,
          response_serializer=weladee__pb2.AddResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.weladee.com.Odoo', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
