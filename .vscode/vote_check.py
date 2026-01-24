def check_eligibility():
    try:
        age = int(input("Enter your age: "))
        if age >= 18:
            print("You are eligible to vote!")
        elif age < 0:
            print("Invalid age entered.")
        else:
            print("You are not eligible to vote yet.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    check_eligibility()

