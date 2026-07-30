# Contidional Statements
# if statement

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible for voting.")
# print("Program completed..")

# if-else statement
# age = int(input("Enter your age"));
# if age>18:
#     print("You are eligible to vote.");
# else:
#     print("You are not eligible to vote.");

# if-elif-else statement

# marks = 90;
# if(marks >=90):
#     grade = "A+";
# elif(marks >= 75):
#     grade = "A";
# elif(marks >= 60):
#     grade = "B";
# elif(marks>= 40):
#     grade = "C";
# else:
#     grade = "Fail";
# print(f"Mark: {marks}, Grade: {grade}");

# Nested Conditions
# age = 12;
# citizenship = "Indian";
# if age >=18:
#     if citizenship == "Indian":
#         print("Eligible to vote in India...");
#     else:
#         print("Not an indian citizen, hence, not eligible to vote in India..");
# else:
#     print("Underage");

# Iteration
#for loop
# Example 1 
# fruits = ["Apple","Banana","Mango"];
# for fruit in fruits:
#     print(fruit);
# print(fruits[0]);

#Example 2
# total = 0
# for num in range(1, 8):
#     total += num
# print(f"Sum: {total}")

#  While Loop : Repeat till condition is true

# counter = 1;
# while counter <= 5:
#     print(counter);
#     counter += 1;
# print();
# print(counter);

# Break Statement
# total = 0;
# for num in range(1, 11):
#     total += num;
#     if total >= 15:
#         print(f"num {num}")
#         break;
# print(f"Total: {total}");

# Continue Statement
# for num in range(1, 6):
#     if num == 2:
#         continue;
#     print(num);

# Pass statement

# for num in range(1,6):
#     if(num == 3):
#         pass; # Placeholder for future code
#     print(num);

students = [
    {"name": "Amit", "marks": 92},
    {"name": "Riya", "marks": 78},
    {"name": "Karan", "marks": 35},
    {"name": "Neha", "marks": 65},
    {"name": "Stop", "marks": 0}
]

for student in students:

    if student["name"] == "Stop":
        break

    marks = student["marks"]

    if marks < 40:
        print(student["name"], "- Failed")
        continue

    if marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    else:
        grade = "C"

    if grade == "A+":
        print(student["name"], "- Excellent")
    else:
        pass

    print(student["name"], "- Grade:", grade)
 
 # List Comprehension: List comprehension is a concise & Python's way 

# Without list comprehension
# numbers = [1,2,3,4,5];
# squares = [];
# for num in numbers:
#     squares.append(num**2);
# print(squares);

#Using List Comprehension
# numbers = [1,2,3,4,5];
# squares = [num**2 for num in numbers];
# print(squares);

# numbers = [1,2,3,4,5];
# Cubes = [num**3 for num in numbers];
# print(Cubes);
# Upper case
# names = ["john", "alice", "bob"]
# upper_names = [name.upper() for name in names]
# print(upper_names)

# Finding Even Numbers
# numbers = range(1, 11)
# evens = [n for n in numbers if n % 2 == 0]
# print(evens)

# Finding Odd number
# numbers = range(1, 11)
# Odds = [n for n in numbers if n % 2 != 0]
# print(Odds)

# Finding odd or even in a list of numbers
numbers = [1, 2, 3, 4, 5]
#########################
# result = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
# result = [f"Even:{n}" if n%2 ==0 else f"odd: [n]" for n in numbers]
# print(result)

# numbers = [10, -5, 20, -8, 30]
# result = [n if n>=0 else 0 for n in numbers];
# print(result);

# Combine values from two lists

# pairs = [];
# Pair1 = ["A","B","C"];
# Pair2 = [1,2,3];
# pairs = [(i,j) for i in Pair1 for j in Pair2];
# print(pairs);

# word = "python";
# chars = [ch for ch in word];
# print(chars);

word = "programming"
vowels = [ch for ch in word if ch.lower() in "aeiou"];
print(vowels);