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
        print(f"You are young")
    elif a <= 18:
        bill += 7
        print(f"You are adult")
    elif a < 45:
        bill += 7
        print(f"You are big adult")

    elif 45 >= a <= 55:
        print("Free of charge")

    else:
        bill += 12
        print(f"Your are super adult")

    return bill

def main():
    choice = int(input("Please enter your height: "))

    if not customer_height(choice):
        return

    age = int(input("Enter your age: "))

    print(f"Your total price: {customer_age(age)}")
    print(f"Enjoy the rides.")

main()
