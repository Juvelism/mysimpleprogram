# TODO: TICKETING

def customer_height(h):

    if h >= 120:

        return True

    else:

        print("You are too short for the rides.")
        return False

def customer_age(a):
    bill = 0
    if a <= 12:
        bill += 5

    return bill

def main():
    choice = int(input("Please enter your height: "))

    if not customer_height(choice):
        return

    age = int(input("Enter your age: "))

    print(f"Your total price: {customer_age(age)}")
    print(f"Enjoy the rides.")

main()
