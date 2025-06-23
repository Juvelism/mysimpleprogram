def get_user_info():
    user_name = input("Full name: ").title()
    user_age = int(input("Age: "))
    return user_name, user_age

def check_category(age):
    if 0 == age <= 12:
        return 'Child'
    elif 13 >= age <= 19:
        return 'Teenager'
    elif 20 >= age <= 59:
        return 'Adult'
    else:
        return 'Senior Citizen'

def print_category(name, category):
    print(f"{name}, you are a {category}.")

def main():
    name, age = get_user_info()
    print_category(name, check_category(age))

main()