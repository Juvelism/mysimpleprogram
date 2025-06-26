
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
            return True
        else:
            return False
    return None


def display_result(users):

    attempts = 3
    while attempts > 0:
        access = check_credentials()

        if access:
            print(f'✅ Access granted. Welcome, {users}')
            break
        else:
            print('❌ Access denied.')
            attempts -= 1
            print(f'{attempts} attempts left.')

def main():
    display_result(check_credentials())

main()