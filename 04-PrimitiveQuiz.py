Questions = {
    "France": "Paris",
    "Spain": "Madrid City",
    "Germany": "Berlin",
    "Ireland": "Dublin",
    "United Kingdom": "London",
    "Italy": "Rome",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Finland": "Helsinki",
    "Denmark": "Copenhagen"
}

Score = 0

for Country, Capital in Questions.items():
    answer = input(f"What is the capital of {Country}? ").strip().lower()
    if answer == Capital.lower():
        print("Correct Answer!\n")
        Score += 1
    else:
        print(f"Wrong Answer! The Correct Answer is {Capital}.\n")

print(f"You scored a total of {Score}/{len(Questions)}!")
