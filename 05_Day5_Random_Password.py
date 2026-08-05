import random
import string

def generate_password(length=12):
    chars = (
        string.ascii_letters+
        string.digits+
        string.punctuation
    )
    return ''.join(random.choice(chars)for _ in range(length))

num_passwords = int(input("How many password do you need? "))
length = int(input("Password length :"))
print("\nGenerate Password: ")
for i in range(num_passwords):
    print(f"{i + 1}.{generate_password(length)}")