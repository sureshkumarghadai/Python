print("Temperature Converter");
print("=====================");
print("1. Celsius to Fahrenheit");
print("2. Fahrenheit to Celsius");

choice = input("Select an option (1 or 2): ");

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "));
    fahrenheit = (celsius * 9 / 5) + 32;
    print(f"{celsius}°C = {fahrenheit:.2f}°F");
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "));
    celsius = (fahrenheit - 32) * 5 / 9;
    print(f"{fahrenheit}°C = {celsius:.2f}°F");
else:
    print("Invalid choice!");