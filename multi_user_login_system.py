
def check_credentials():

    admin_credentials = {
        'admin1': 'admin123',
        'admin2': 'admin456',
        'admin3': 'admin789'
    }

    user = input("Username: ")
    password = input("Password: ")

    for i in admin_credentials:
        if user == i and password == admin_credentials[i]:
            return user

    return False


def display_result():

    print("-- ADMIN LOGIN --")
    attempts = 3
    while attempts > 0:
        user =  check_credentials()

        if user:
            print(f'✅ Access granted. Welcome, {user}')
            break
        else:
            attempts -= 1
            print(f'❌ Access denied. {attempts} attempts left.')


def main():
   display_result()
main()