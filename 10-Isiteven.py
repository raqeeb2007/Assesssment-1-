def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even."
    else:
        return f"{number} is Odd."

def main():
    try:
        num = int(input("Input a Number:"))
        result = check_even_odd(num)
        print(result)
    except ValueError:
        print("Invalid Input. Please try again and make sure inputted value is a whole number.")

if __name__ == "__main__":
    main()