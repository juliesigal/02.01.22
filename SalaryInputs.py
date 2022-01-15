class SalaryInputs:

    def get_salary(self):
        salary = input('please enter a salary')
        return salary
        
        # if the amount is not float raise valueError
        # hint: float(amount)
        # if amount > 100_000 raise TooHigherError
        # if amount < 10_000 raise TooLowerError
        # else return amount * 2