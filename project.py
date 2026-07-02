employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Aditi', 'age': 24, 'department': 'IT', 'salary': 65000},
    103: {'name': 'Rohan', 'age': 30, 'department': 'Finance', 'salary': 72000},
}

def add_employee():
    print("\n--- Add New Employee ---")

    
    while True:
        emp_id_input = input("Enter Employee ID: ").strip()
        if not emp_id_input.isdigit():
            print("Invalid input. Employee ID must be a number.")
            continue
        emp_id = int(emp_id_input)
        if emp_id in employees:
            print(f"Employee ID {emp_id} already exists. Please enter a new ID.")
        else:
            break
    name = input("Enter Employee Name: ").strip()
    while True:
        age_input = input("Enter Employee Age: ").strip()
        if age_input.isdigit() and int(age_input) > 0:
            age = int(age_input)
            break
        print("Invalid input. Please enter a valid positive number for age.")

    department = input("Enter Employee Department: ").strip()
 while True:
        salary_input = input("Enter Employee Salary: ").strip()
        try:
            salary = float(salary_input)
            if salary < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive number for salary.")

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print(f"\nEmployee '{name}' (ID: {emp_id}) added successfully!")

def view_employees():
    print("\n--- All Employees ---")

    if not employees:
        print("No employees available.")
        return

    # Table header
    print(f"{'ID':<8}{'Name':<15}{'Age':<6}{'Department':<15}{'Salary':<10}")
    print("-" * 54)

    for emp_id, details in employees.items():
        print(f"{emp_id:<8}{details['name']:<15}{details['age']:<6}"
              f"{details['department']:<15}{details['salary']:<10.2f}")

def search_employee():
    print("\n--- Search Employee ---")

    emp_id_input = input("Enter Employee ID to search: ").strip()
    if not emp_id_input.isdigit():
        print("Invalid input. Employee ID must be a number.")
        return

    emp_id = int(emp_id_input)

    if emp_id in employees:
        details = employees[emp_id]
        print(f"\nEmployee Found (ID: {emp_id})")
        print(f"Name       : {details['name']}")
        print(f"Age        : {details['age']}")
        print(f"Department : {details['department']}")
        print(f"Salary     : {details['salary']:.2f}")
    else:
        print("Employee not found.")

def main_menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("\nThank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 4.")


# ------------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------------
if __name__ == "__main__":
    main_menu()
