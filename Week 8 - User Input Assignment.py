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
    # 1. Employee ID (required, digits only, 1 to 7 digits long)
    emp_id = input("Enter Employee ID: ").strip()
    if not emp_id or not emp_id.isdigit() or len(emp_id) > 7:
        print("Invalid Employee ID. It is required and must be a number up to 7 digits long.")
        return

    # 2. Employee Name (required, primarily letters, no forbidden characters)
    forbidden_name_chars = set('!"@#$%^&*()_=+,<>/?;:[]{}\\')
    emp_name = input("Enter Employee Name: ").strip()
    if not emp_name or not is_primarily_alpha(emp_name) or has_forbidden_chars(emp_name, forbidden_name_chars):
        print("Invalid Employee Name. Please enter a valid name using primarily letters.")
        return

    # 3. Employee Email Address (required, primarily alphanumeric, no forbidden characters)
    forbidden_email_chars = set('!"\'#$%^&*(),=+<>/\;[]{}?')
    # Include ':' as well per specification
    forbidden_email_chars.add(":")
    emp_email = input("Enter Employee Email Address: ").strip()
    if not emp_email or not is_primarily_alnum(emp_email) or has_forbidden_chars(emp_email, forbidden_email_chars):
        print("Invalid Employee Email Address. Please enter a valid email address.")
        return

    # 4. Employee Address (optional; if provided, primarily alphanumeric and no forbidden characters)
    forbidden_address_chars = set('!"\'@$%^&*_=+<>?;:[]{}')
    emp_address = input("Enter Employee Address (optional): ").strip()
    if emp_address != "":
        if not is_primarily_alnum(emp_address) or has_forbidden_chars(emp_address, forbidden_address_chars):
            print("Invalid Employee Address. Please enter a valid address or leave it blank.")
            return
        address_sentence = f"Your address is {emp_address}"
    else:
        address_sentence = "You did not provide an address."

    # Final output
    print(f"Hello, {emp_name}. Your Employee ID is {emp_id}, and your email address is {emp_email}. {address_sentence}")


if __name__ == "__main__":
    main()