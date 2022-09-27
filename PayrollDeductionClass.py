class PayrollDeduction:

    def __init__(self,description, date, charge_amount,employee_ID):
        self.__description=description
        self.__date=date
        self.__charge_amount=charge_amount
        self.__employee_ID=employee_ID

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_charge_amount(self):
        return self.__charge_amount

    def get_employee_ID(self):
        return self.__employee_ID