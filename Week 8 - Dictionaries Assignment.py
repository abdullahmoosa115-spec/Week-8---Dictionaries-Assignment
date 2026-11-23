# =====================================================================
# Prepare the lists from last week's program
# =====================================================================
raw_data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# Separate unique employee numbers, names, and salaries from raw_data
employee_numbers = []
employee_names = []
employee_salaries = []

for item in raw_data:
    if isinstance(item, int) and item > 1000:
        if item not in employee_numbers:
            employee_numbers.append(item)
    elif isinstance(item, str):
        if item not in employee_names:
            employee_names.append(item)
    elif isinstance(item, float):
        if item not in employee_salaries:
            employee_salaries.append(item)

# Calculate total hourly rate (base wage * 1.3) for each salary
total_hourly_rate = []
for wage in employee_salaries:
    total_hourly_rate.append(wage * 1.3)

# Calculate company raises based on salary brackets
company_raises = []
for wage in employee_salaries:
    if 22 <= wage < 24:
        raise_amount = wage * 0.05
    elif 24 <= wage < 26:
        raise_amount = wage * 0.04
    elif 26 <= wage < 28:
        raise_amount = wage * 0.03
    else:
        raise_amount = wage * 0.02

    company_raises.append(wage + raise_amount)

# =====================================================================
# Week 8 Requirement: Combine lists into a list of dictionaries
# =====================================================================
# Initialize the list that will store each employee dictionary
employee_records = []

# Iterate by index to pair matching values from each list into one dictionary
for i in range(len(employee_numbers)):
    employee_dict = {
        "employee_number": employee_numbers[i],
        "employee_name": employee_names[i],
        "employee_salary": employee_salaries[i],
        "total_hourly_rate": total_hourly_rate[i],
        "company_raise": company_raises[i]
    }
    employee_records.append(employee_dict)

# Print the final list of dictionaries at the end of the program
print(employee_records)