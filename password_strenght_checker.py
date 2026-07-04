password = input("Enter a password: ")
has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    print(ch)
    if ch.islower():
        has_lower = True
    if ch.isupper():
        has_upper = True
    if ch.isdigit():
        has_digit = True
    if ch in "!@#$%^&*()-+":
        has_special = True
    if len(password)<8:  
        print("password should be at least 8 characters long" )   
    if not has_upper:
        print("Missing uppercase letter(A_Z)") 
    if not has_lower:
        print("Missing lowecase letter(a-z)")
    if not has_digit:
        print("Missing digit(0-9)")
    if not has_special:
        print("Missing special character(!@#$%^&*()-+)") 
                      
    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
       print("strong password")
else:
    print("Weak password")