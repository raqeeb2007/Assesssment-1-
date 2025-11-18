days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

month = int(input("Input Number For Month (1-12): "))

if 1 <= month <= 12:
    days = days_in_month[month]
    if month == 2:
        leap = input("Leap Year? (yes/no): ").lower()
        if leap == "yes":
            days = 29
    print(f"Mentioned {month} Has {days} Days.")
else:
    print("Invalid Input.")