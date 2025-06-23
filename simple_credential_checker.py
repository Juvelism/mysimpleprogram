def get_credentials():
    username = input("Username: ")
    password = input("Password: ")

    return username, password

def check_login(user, password):
    u_name = 'admin'
    pw = '1234'

    if user == u_name and password == pw:
        return 'Access Granted!'
    else:
        return 'Access Denied!'

def print_login_result(success):
    print(f'{success}')


def main():
    user, password = get_credentials()
    print_login_result(check_login(user,password))

main()