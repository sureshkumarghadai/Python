# lottery_system.py

import random

participants = [
    "John",
    "Mary",
    "David",
    "Sophia",
    "Alex",
    "Robert"
]

while True:

    print("\n=======================")
    print("ONLINE LOTTERY SYSTEM")
    print("=======================")

    print("1. Generate Lucky Number")
    print("2. Select Random Winner")
    print("3. Generate OTP")
    print("4. Shuffle Participants")
    print("5. Exit")

    option = input("Enter Choice: ")

    if option == "1":

        lucky_number = random.randint(1, 100)

        print("Lucky Number =", lucky_number)

    elif option == "2":

        winner = random.choice(participants)

        print("Winner =", winner)

    elif option == "3":

        otp = random.randint(100000, 999999)

        print("OTP =", otp)

    elif option == "4":

        random.shuffle(participants)

        print("\nParticipants Order")

        for p in participants:
            print(p)

    elif option == "5":

        print("Lottery Closed")
        break

    else:

        print("Invalid Selection")
 