# Data Structures : Python provides several built-in data structures that enable different & efficient storage. organization and manupulation of data . These structures form the foundation of python programming and are used to represent collections of values in different ways depending on requirements i.g ordering, mutablity, uniqueness, & key-value based access.
#Type of data Python data structures: Lists, Tuples, sets, Dictionaries, Nested Structures
# List: A list is an ordered , mutable collection of elements.IT is one of the most frequently used data structures in Python because of its flexibility & ability to store multiple items in a single variable.
#Characterstics of Lists : Ordered, Mutable (Able to change),Dynamic size, Indexed, Heterogenous storage, Duplicates value allowed,.
#Internal behaviour: Python lists are implemented as dynamic arrays. Memory allocation is managed automatically by the python runtime. This allows moste efficient access to elements by position while supporting, resizing operations.
#Common operations: Addition of elements, Removing elements, Update elements, Searching for elments, Sorting data , Reverse order, Traversing elements, Slicing subsets of data, Combining lists.
#Advantages of List:easy to use & highly flexible, Suports a wide range of operations, Efficient positional access, Suitable for sequential data management
# Limitations: Requires more memory that some specialized structures. Search operation can because slower with vey large collections, Insertion and deletion in the middle may required shifting of elements 

# Tuples: A tuple is an ordered, immutable collection of alements. it provides a way to group related values that should remain unchanged after creation.
#Characterstics of Tuples: Ordered, Immutable, Indexed, Heterogenous Storage, Duplicate values allowed.
#Internal behaviour of Tuples: Tuples are optimized for fixed collection of data. Because they are immtable phyon can manage memorey more efficiently compared to mutable structure
#Common Use Case: Storing fixed data, returning multiple value from the functions, protecting data from accidental modification, Representing structured records
# Advantages of Tuples: Faster than lists in many operations, Memory efficient, Data integrity through immutability and Can be used as keys in dictionaries when containing immutable elements
#Limitations : Can't be modified after creation, Less flexible than than lists for dynamic data
# Sets: A set is an unordered collection of unique elements.It is designed primarily for membership testing & mathematical set operations
#Characterstics of Sets: Unordered, Mutable, Unique elements, Fast membership testing
#Internal Behavior: Sets are implemented using hash table, allowing quick insertion , deletion , search operations
#Common operations of Sets: Adding elements, Removing elements, Testing memebership, union, intersection, difference, Symmetric difference, 
# Advantages of sets: Fast lookup, automatic duplicate removal, excellent for comparision operation, Efficient handling of unique collections
# Limitations: No indexing support, Unordered nature may bot suit sequence-based requirements, Elements must be hashable
# Dictionaries: A dictionary is a mutable collection that stores data as key-value pairs. It allows efficient retrieval of values based on associated keys.
#Characterstics of Dictionaries: Key-value data structure, Mutable, Fast access, Unique keys, Dynamic size, Ordered, 
#Internal behaviour of Dictionaries: Dictionaries are implemented as hash tables. A hash function converts each key into a storage location, enabling rapid access to specified value.
# Common Operations of Dictionary: Creating entries, updatingentries, removing entries, Looking up values, Iterating through keys & values, Check key existence, Merge dictionaries, 
#Advantages of Dictionaries: Extremely fast retrieval, Clear representaion of relationships, Fexible storage model, Efficient data orginazion,
#Limitaions of Dictionaries: Keys must be unique, Keys must be immutable and hashable, Uses more memory that some sequential data structures
# Nested Structures: A nested structure is a data structure that contains one or more data structures within another. Nesting allows representation of complex & hierachical relationships. 
#Types of nesting: List within List, Tuple within Tuple, Set within other data structure, Dictionary within dictionary, Mixed nesting
#Characteristics: Hierachical orginazation, Multi-level access, Greater flexibility, Scalability 
# Benefits: Improved organizational of complex information, Better representation of hierarchical relationships, increased flexibility in data modelling, Ability to group related information logically 
# List Example
# Student Marks Manager using Lists

# students = []

# while True:
#     print("\n===== STUDENT Perormance Dashboard =====")
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

# Employee Records using Tuples

# employees = [
#     (101, "John", "HR"),
#     (102, "Mary", "Finance"),
#     (103, "David", "IT"),
#     (104, "Sophia", "Marketing")
# ]

# print("===== EMPLOYEE Dashboard =====")

# for emp in employees:
#     emp_id, name, department = emp

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

# Website Visitor Tracker using Sets

visitors = set()

while True:
    print("\n===== Visitor Tracker =====")
    print("1. Add Visitor")
    print("2. View Visitors")
    print("3. Check Visitor")
    print("4. Remove Visitor")
    print("5. Total Visitors")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        visitor = input("Enter visitor name: ")
        visitors.add(visitor)
        print("Visitor recorded.")

    elif choice == "2":
        print("\nUnique Visitors:")

        for visitor in visitors:
            print(visitor)

    elif choice == "3":
        visitor = input("Enter name to search: ")

        if visitor in visitors:
            print("Visitor exists.")
        else:
            print("Visitor not found.")

    elif choice == "4":
        visitor = input("Enter visitor name: ")

        if visitor in visitors:
            visitors.remove(visitor)
            print("Visitor removed.")
        else:
            print("Visitor not found.")

    elif choice == "5":
        print("Total Unique Visitors:", len(visitors))

    elif choice == "6":
        print("Application Closed.")
        break

    else:
        print("Invalid Choice")
 