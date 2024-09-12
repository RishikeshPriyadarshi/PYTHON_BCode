'''
Exercise: Validate user input
         
        1. Username is not more than 12 chars
        2. Username must not contain space
        3. Username must not contain digits

'''

username = input("Enter a usernmae: ")

if len(username) > 12:
    print("Your username can't be more than 12 chars ")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces ")    
elif not username.isalpha() :
    print("Your user name must not contain digits")    
else:
    print(f"welcome {username}")    
