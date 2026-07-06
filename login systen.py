while True:
    print("1. Username")
    print("2. Password")
    print("3. Exit")
    
    choice = int(input("Enter a Choice: "))
    if choice == 1:
        name = input("Enter a Usernaname ")
        password = input("Enter a Password ")
        
        file = open("note.txt","a")
        content = file.write(name +"," + password +"\n")
        file.close()
        print("User Register successfully")

    elif choice == 2:
        name = input("Enter a Usernaname ")
        password = input("Enter a Password ")
        
        file = open("note.txt","r")
        line = file.read()
        file.close()
        
        found = False
        for ch in line:
            username,saved_password = line.strip().split(",")
            
        if name == username and password  == saved_password:
            found = True    
            break
        if found:
            print("lodin sucessfully")
        else:
            print("invalid username or password")
             
    elif choice == 3:
        print("Thankyou")   
        break      
    else:
        print("invalid choice")        
            
            
            
            