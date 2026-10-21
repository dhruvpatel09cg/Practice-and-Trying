password = "Abc@123"
attempt = 1
while attempt<=4:
    user = input("Enter Password:")
    if user==password:
        print("Login Successful!")
        break
    print("Incorrect Password!")
    print("Remaining Attempts:",4-attempt)
    attempt += 1
if attempt == 5:
    print("You are blocked!")
