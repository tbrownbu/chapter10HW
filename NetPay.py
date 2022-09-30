import PayrollDeductionClass as p
import EmployeeClass as e

employee = e.employee('Jimmy Smith', 58475, 'Information Systems','Developer',6800)

deduction1 = p.PayrollDeduction('food court','8/14/2022',22.50, 39119)
deduction2 = p.PayrollDeduction('gift contribution', '8/12/2022',25.00,58475)
deduction3 = p.PayrollDeduction('food court','8/17/2022',15.25,21547)
deductoin4 = p.PayrollDeduction('vending machine','8/22/2022', 3.00, 58475)
deduction5 = p.PayrollDeduction('vending machine', '8/5/2022', 2.75,58475)

print('***Employee Pay***')
print('Employee Name:', employee.get_name())
print('ID number:', employee.get_ID_number())
print('Department:', employee.get_department())
print('Gross Pay: $', float(employee.get_salary()), sep='')

net_pay =employee.get_salary()

deductions = [deduction1,deduction2,deduction3,deductoin4,deduction5]

for x in deductions:
    if p.PayrollDeduction.get_employee_ID(x) == employee.get_ID_number():
        net_pay-=p.PayrollDeduction.get_charge_amount(x)
print('Net Pay: $',net_pay, sep='')