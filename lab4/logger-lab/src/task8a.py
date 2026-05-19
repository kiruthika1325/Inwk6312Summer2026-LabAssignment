class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        # This defines how the error looks when printed
        return f'{self.salary} -> {self.message}'

# --- Start of Program ---

try:
    # 1. Take user input
    user_input = input("Enter salary amount: ")
    salary = int(user_input)

    # 2. Check the range constraint
    if not 5000 < salary < 15000:
        # Raise the custom exception defined above
        raise SalaryNotInRangeError(salary)
    
    # 3. If no exception is raised, print success
    print(f"Success! Salary of {salary} is accepted.")

except SalaryNotInRangeError as e:
    # Catch the custom error and print the __str__ result
    print(f"Custom Error: {e}")

except ValueError:
    # Catch cases where the user enters text instead of a number
    print("Invalid Input: Please enter a whole number.")
