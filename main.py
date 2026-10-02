import random
import string
from password_generator import password_msg, view_saved_passwords

welcome_msg = '''
    ******************************
      🔐 PASSWORD GENERATOR 🔐
    ******************************

    🟢Status : Encrypted
'''
command_msg = '''
    [G] ➡  Generate Password
    [V] ➡  View Saved Passwords
    [Q] ➡  Quit
'''

def main():
    print(welcome_msg)
    while True:
        print(command_msg)
        command = input("Enter your command: ").strip().upper()
        if command == "G":
            password_msg()
        elif command == "V":
            view_saved_passwords()
        elif command == "Q":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid command. Please try again.")

if __name__ == "__main__":
    main()