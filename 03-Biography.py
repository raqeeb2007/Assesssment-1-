Name = input("Enter Your Full Name:")
Hometown = input("Enter Your Hometown:")

while True:
    Age_input = input("Enter Your Age:")
    if Age_input.isdigit():
        Age = int(Age_input)
        break
    else:
        print("Please input a valid number for your Age")

Biography = {
    "Name" : Name,
    "Hometown" : Hometown,
    "Age" : Age
}

print(Biography["Name"], Biography["Hometown"], Biography["Age"], sep="\n")
