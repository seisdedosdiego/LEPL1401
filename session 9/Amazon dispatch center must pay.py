class EmployeeDidntWorked(Exception):
    pass

class EmployeeWorkedNegatively(Exception):
    pass

class EmployeeWorkedTooMuch(Exception):
    pass

class PayIsNegative(Exception):
    pass

class PayIsTooBig(Exception):
    pass

def pay_employee(employee, hours_worked):
    """ Spécialisations """
   
    if hours_worked == 0:
        raise EmployeeDidntWorked("EmployeeDidntWorked")
    if hours_worked < 0:
        raise EmployeeWorkedNegatively("EmployeeWorkedNegatively")
    if hours_worked > 744:
        raise EmployeeWorkedTooMuch("EmployeeWorkedTooMuch")
    if employee.pay < 0:
        raise PayIsNegative("PayIsNegative")
    if employee.pay > 100:
        raise PayIsTooBig("PayIsTooBig")

    salary = employee.pay * hours_worked
    employee.receive_salary(salary)