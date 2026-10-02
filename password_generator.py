import random
import string
import time

saved_passwords =[]

def password_generator():
    try:
        length = input("Length of password you want to generate: ")
        length = int(length)
        if length < 5:
            print("Length must be greater than 5.")
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = "".join(random.choice(characters) for _ in range(length))
            return(password)
    except ValueError:
        print("💀Length must explicitly be a number.")

def password_msg():
    password = password_generator()
    saved_passwords.append(password)
    if any(char in string.ascii_letters for char in password):
        print("\t[✔] Letters    a-z")
    if any(char in string.digits for char in password):
        print("\t[✔] Numbers    0-9")

    if any(char in string.punctuation for char in password):
        print("\t[✔] Symbols    @!#$")
    for _ in range(3):
        time.sleep(0.6)
        print(".", end="", flush=True)
    print("\n")
    print("\t________________________________")
    print("\t💬 Password Generated ") 
    print("\t________________________________")
    print(f"\tLength of password: {len(password)}")
    print("\t________________________________")
    print(f"\t🔒 {password}") 
    print("\t________________________________")
    print("\t💬 Password Generated Successfully")

def view_saved_passwords():
    if not saved_passwords:
        print("\t💬 No saved passwords.")
    else:
        print("\t💬 Saved Passwords:")
        for index, password in enumerate(saved_passwords, start=1):
            print(f"\t{index}. {password}")