admin_credentials = {
    'admin1': 'admin123',
    'admin2': 'admin456',
    'admin3': 'admin789'
}

def get_login_input():
    user = input("Username: ")
    password = input("Password: ")

    return user, password

def check_credentials(user_name,user_pass):
    count
    for i in admin_credentials:
        if user_name in admin_credentials and user_pass in admin_credentials[i]:
            return '✅ Access granted'
        else:
            return  '❌ Access denied'

    return False

def display_result(access, message):

    print(f'Welcome. {access}')

def main():
    user, password = get_login_input()
    check_credentials(user, password)

main()
