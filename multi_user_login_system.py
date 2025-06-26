
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
        else:
            return False
    return None


def display_result():

    attempts = 3
    while attempts > 0:
        user =  check_credentials()

        if user:
            print(f'✅ Access granted. Welcome, {user}')
            break
        else:
            print('❌ Access denied.')
            attempts -= 1
            print(f'{attempts} attempts left.')

def main():
   display_result()


main()