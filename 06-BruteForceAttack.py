Correct_Password = "12345"

Password = input("Enter Password: ")

while Password != Correct_Password:
    print("Incorrect Password Inputted. Try Again.")
    Password = input("Enter Password: ")

print("Correct Password Inputted! Welcome.")