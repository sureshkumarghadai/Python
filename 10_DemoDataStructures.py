# List example
# Student Marks Manager using Lists

# students = []

# while True:
#     print("\n===== STUDENT MARKS MANAGER =====")
#     print("1. Add Student")
#     print("2. View Students")
#     print("3. Update Student")
#     print("4. Delete Student")
#     print("5. Sort Students")
#     print("6. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         name = input("Enter student name: ")
#         students.append(name)
#         print("Student added successfully!")

#     elif choice == "2":
#         print("\nStudent List:")
#         for i, student in enumerate(students, start=1):
#             print(f"{i}. {student}")

#     elif choice == "3":
#         old_name = input("Enter existing student name: ")

#         if old_name in students:
#             new_name = input("Enter new name: ")
#             index = students.index(old_name)
#             students[index] = new_name
#             print("Student updated successfully!")
#         else:
#             print("Student not found.")

#     elif choice == "4":
#         name = input("Enter student name to delete: ")

#         if name in students:
#             students.remove(name)
#             print("Student deleted.")
#         else:
#             print("Student not found.")

#     elif choice == "5":
#         students.sort()
#         print("Students sorted alphabetically.")

#     elif choice == "6":
#         print("Exiting application...")
#         break

#     else:
#         print("Invalid choice.")


# Tuple example
# Employee Records using Tuples

# employees = [
#     (101, "John", "HR"),
#     (102, "Mary", "Finance"),
#     (103, "David", "IT"),
#     (104, "Sophia", "Marketing")
# ]

# print("===== EMPLOYEE DIRECTORY =====")

# for emp in employees:
#     emp_id, name, department = emp  # object destructuring

#     print(f"""
# Employee ID : {emp_id}
# Name        : {name}
# Department  : {department}
# """)

# search_id = int(input("Enter Employee ID to search: "))

# found = False

# for emp in employees:
#     if emp[0] == search_id:
#         print("\nEmployee Found")
#         print(f"ID: {emp[0]}")
#         print(f"Name: {emp[1]}")
#         print(f"Department: {emp[2]}")
#         found = True
#         break

# if not found:
#     print("Employee not found.")


# Set example
# Website Visitor Tracker using Sets

# visitors = set()

# while True:
#     print("\n===== VISITOR TRACKER =====")
#     print("1. Add Visitor")
#     print("2. View Visitors")
#     print("3. Check Visitor")
#     print("4. Remove Visitor")
#     print("5. Total Visitors")
#     print("6. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         visitor = input("Enter visitor name: ")
#         visitors.add(visitor)
#         print("Visitor recorded.")

#     elif choice == "2":
#         print("\nUnique Visitors:")
        
#         for person in visitors:
#             print(person)

#     elif choice == "3":
#         visitor = input("Enter name to search: ")

#         if visitor in visitors:
#             print("Visitor exists.")
#         else:
#             print("Visitor not found.")

#     elif choice == "4":
#         visitor = input("Enter visitor name: ")

#         if visitor in visitors:
#             visitors.remove(visitor)
#             print("Visitor removed.")
#         else:
#             print("Visitor not found.")

#     elif choice == "5":
#         print("Total Unique Visitors:", len(visitors))

#     elif choice == "6":
#         print("Application Closed.")
#         break

#     else:
#         print("Invalid Choice")


# Dictionary Example
# Inventory Management System

# inventory = {}

# print(type(inventory))  # <class 'dict'>

# while True:
#     print("\n===== INVENTORY MANAGEMENT =====")
#     print("1. Add Product")
#     print("2. View Products")
#     print("3. Update Quantity")
#     print("4. Delete Product")
#     print("5. Search Product")
#     print("6. Exit")

#     choice = input("Choose Option: ")

#     if choice == "1":
#         product = input("Enter product name: ")
#         quantity = int(input("Enter quantity: "))

#         inventory[product] = quantity
#         print("Product added successfully.")

#     elif choice == "2":
#         print("\nAvailable Products")

#         for product, qty in inventory.items():
#             print(f"{product}: {qty}")

#     elif choice == "3":
#         product = input("Enter product name: ")

#         if product in inventory:
#             quantity = int(input("Enter new quantity: "))
#             inventory[product] = quantity
#             print("Quantity updated.")
#         else:
#             print("Product not found.")

#     elif choice == "4":
#         product = input("Enter product name: ")

#         if product in inventory:
#             del inventory[product]
#             print("Product deleted.")
#         else:
#             print("Product not found.")

#     elif choice == "5":
#         product = input("Enter product name: ")

#         if product in inventory:
#             print("Quantity:", inventory[product])
#         else:
#             print("Product not available.")

#     elif choice == "6":
#         break

#     else:
#         print("Invalid Choice")


# Nested Data Structures Example
# University Management System

university = {
    "CS101": {
        "course_name": "Computer Science",
        "students": ["John", "Mary", "David"]
    },
    "CS102": {
        "course_name": "Data Science",
        "students": ["Sophia", "Alex"]
    }
}

while True:
    print("\n===== UNIVERSITY MANAGEMENT =====")
    print("1. View Courses")
    print("2. View Students")
    print("3. Add Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nCourses")

        for course, details in university.items():
            print(course, "-", details["course_name"])

    elif choice == "2":
        course = input("Enter course code: ")

        if course in university:
            print("\nStudents")

            for student in university[course]["students"]:
                print(student)
        else:
            print("Course not found.")

    elif choice == "3":
        course = input("Enter course code: ")

        if course in university:
            student = input("Enter student name: ")
            university[course]["students"].append(student)
            print("Student added.")
        else:
            print("Course not found.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")