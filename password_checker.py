#password_strenth_checher 

import re

def check_password_strength(password):
    if len(password) <9:
        return"Weak: password must be at least 9 chars"
    
    if not any(char.isdigit() for char in password):
        return "Weak: password must have at least one digit"
    
    if not any(char.isupper() for char in password):
        return "Weak: password must contain an upper char"
    
    if not any(char.islower() for char in password):
        return "Weak: password must contain a lower char"
    
    if not re.search(r'[!@#$%^&*()-_=+\|,{};:/?.]',password):
       return "Medium: password must contain a special char"

    return "Strong: Your password is secured!"


def password_checher():
    print("welcome to the password strength checker")

    while True:
        password = input("enter your password(or tye 'EXIT' to quit): ")
        if password.lower() == "exit":
            print("thank you for using this tool")
            break 

        result = check_password_strength(password)
        print(result)


#run the password checker tool 
if __name__== "__main__":
    password_checher() 