def has_forbidden_chars(text, forbidden_chars):
    """Return True if any character in text appears in forbidden_chars."""
    for char in text:
        if char in forbidden_chars:
            return True
    return False


def is_primarily_alpha(text):
    """Return True if more than half of the characters in text are letters."""
    if not text:
        return False
    letter_count = sum(1 for char in text if char.isalpha())
    return letter_count > len(text) / 2


def is_primarily_alnum(text):
    """Return True if more than half of the characters in text are alphanumeric."""
    if not text:
        return False
    alnum_count = sum(1 for char in text if char.isalnum())
    return alnum_count > len(text) / 2


def main():
    # Forbidden character sets defined once for reuse across employees
    forbidden_name_chars = set(r'!"@#$%^&*()_=+,<>/?;:[]{}' + "\\")
    forbidden_email_chars = set(r"""!"'#$%^&*(),=+<>/?:;[]{}""" + "\\")
    forbidden_address_chars = set(r"""!"'@$%^&*_=+<>?;:[]{}""")

    # List of dictionaries to hold up to 5 employee records
    employees = []
    max_employees = 5

    # Loop up to the maximum allowed number of employees
    for emp_index in range(max_employees):
        print(f"\n--- Entering data for Employee {emp_index + 1} of {max_employees} ---")

        # 1. Employee ID: required, numeric, up to 7 digits (re-prompt until valid)
        while True:
            emp_id = input("Enter Employee ID: ").strip()
            if emp_id and emp_id.isdigit() and len(emp_id) <= 7:
                break
            print("Invalid Employee ID. It is required and must be a number up to 7 digits long. Please try again.")

        # 2. Employee Name: required, primarily letters, no forbidden characters (re-prompt until valid)
        while True:
            emp_name = input("Enter Employee Name: ").strip()
            if emp_name and is_primarily_alpha(emp_name) and not has_forbidden_chars(emp_name, forbidden_name_chars):
                break
            print("Invalid Employee Name. Please enter a valid name using primarily letters. Please try again.")

        # 3. Employee Email Address: required, primarily alphanumeric, no forbidden characters (re-prompt until valid)
        while True:
            emp_email = input("Enter Employee Email Address: ").strip()
            if emp_email and is_primarily_alnum(emp_email) and not has_forbidden_chars(emp_email, forbidden_email_chars):
                break
            print("Invalid Employee Email Address. Please enter a valid email address. Please try again.")

        # 4. Employee Address: optional; if provided, must be primarily alphanumeric without forbidden chars
        while True:
            emp_address = input("Enter Employee Address (optional): ").strip()
            if emp_address == "":
                address_value = None
                break
            if is_primarily_alnum(emp_address) and not has_forbidden_chars(emp_address, forbidden_address_chars):
                address_value = emp_address
                break
            print("Invalid Employee Address. Please enter a valid address or leave it blank. Please try again.")

        # Structure this employee's data as a dictionary and append to the list
        employee_record = {
            "employee_id": emp_id,
            "employee_name": emp_name,
            "employee_email": emp_email,
            "employee_address": address_value
        }
        employees.append(employee_record)

        # Ask whether to add another employee if we haven't reached the 5-employee cap
        if emp_index < max_employees - 1:
            add_more = input("Would you like to enter another employee? (Y/N): ").strip().upper()
            if add_more != "Y":
                break

    # Print out the final list of employee dictionaries at the end of the program
    print("\nFinal Employee List:")
    print(employees)


if __name__ == "__main__":
    main()