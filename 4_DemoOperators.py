# Arithmetic Operators
# a = 10;
# b = 3;

# print(a + b);
# print(a - b);
# print(a * b);
# print(a / b);
# print(a % b);
# print(a // b); # Floor Division Operator
# print(a ** b); # Power

# Comparison Operators
# a = 10;
# b = 20;

# print(a == b); # False
# print(a != b); # True
# print(a > b); # False
# print(a < b); # True
# print(a >= b); # False
# print(a <= b); # True

# Logical Operators (and, or, not)
# age = 20;
# salary = 60000;

# print(age > 18 and salary > 50000); # True

# print(age > 30 or salary > 50000); # True

# is_active = True;
# print(not is_active); # False

# print(not (age > 30) or salary < 50000); # True

# Assignment Operators
# x = 10; # Regular assignment operator
# x += 5; # Compound assignment operator
# print(x); # 15

# x -= 2; # Compound assignment operator
# print(x);

# x *= 3; # Compound assignment operator
# print(x);

# x //= 2; # Compound assignment operator
# print(x);

# x %= 4; # Compound assignment operator
# print(x);

# x **= 5; # Compound assignment operator
# print(x);

# Membership Operators(in, not in)
# name = "Saket Karnik";
# print("S" in name); # True
# print("Kar" in name); # True

# print("R" not in name); 
# print("Kar" not in name);

# Identity Operators (is, is not)
a = [1, 2, 3];
b = a;
c = [1, 2, 3];

print(a is b); # Reference check
print(a==b); # Value Check
print(c is a);
print(c == a);

print(a is not b);
print(c is not a);