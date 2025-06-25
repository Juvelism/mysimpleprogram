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

    for i in admin_credentials:
        if user_name == i and user_pass == admin_credentials[i]:
            return True
        else:
            return False
    return None


def display_result(access, username):
    if access:
        print(f'✅ Access granted. Welcome, {username}')
    else:
        print('❌ Access denied.')


def main():
    user, password = get_login_input()
    display_result(check_credentials(user, password), user)



main()
