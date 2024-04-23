import csv

student_fields = ['ID', 'Name', 'Age', 'Email', 'Phone', 'City']
student_database = 'students.csv'


def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")


def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)
    with open(student_database, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(student_data)
    print("Data saved successfully")


def view_students():
    print("--- Student Records ---")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        max_lengths = [len(field) for field in student_fields]
        data = []
        for row in reader:
            data.append(row)
            for i, value in enumerate(row):
                max_lengths[i] = max(max_lengths[i], len(value))
        print("  ".join(
            f"{field:<{max_lengths[i]}}" for i, field in enumerate(student_fields)))
        print("-" * sum(max_lengths) + "----")
        for row in data:
            print(
                "  ".join(f"{value:<{max_lengths[i]}}" for i, value in enumerate(row)))


def search_student():
    print("--- Search Student ---")
    roll = input("Enter ID to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and roll == row[0]:
                print("----- Student Found -----")
                for i in range(len(student_fields)):
                    print(f"{student_fields[i]}: {row[i]}")
                return
        print("ID not found in our database")


def update_student():
    print("--- Update Student ---")
    roll = input("Enter ID to update: ")
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        student_found = False
        for row in reader:
            if row and roll == row[0]:
                student_found = True
                print("Student Found:")
                updated_row = []
                for i, value in enumerate(row):
                    new_value = input(
                        f"Enter new {student_fields[i]} ({value}): ")
                    updated_row.append(new_value if new_value else value)
                updated_data.append(updated_row)
            else:
                updated_data.append(row)
        if student_found:
            with open(student_database, "w", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("Student updated successfully")
        else:
            print("ID not found in our database")


def delete_student():
    print("--- Delete Student ---")
    roll = input("Enter ID to delete: ")
    updated_data = []
    student_found = False
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and roll != row[0]:
                updated_data.append(row)
            elif row:
                student_found = True
    if student_found:
        with open(student_database, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID", roll, "deleted successfully")
    else:
        print("ID not found in our database")


while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        break
    else:
        print("Invalid choice!")

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
