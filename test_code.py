# Code here
from itertools import count

admin_credentials = {
    'admin1': 'admin123',
    'admin2': 'admin456',
    'admin3': 'admin789'
}

def get_login_input():
    user = input("Username: ")
    password = input("Password: ")

    return user, password

def number_of_attempt(n_attempt):
     counts = 0

     if n_attempt != 3:
         counts += 1

     return counts

def check_credentials(user_name,user_pass):

    for i in admin_credentials:
        if user_name in i and user_pass in admin_credentials[i]:
            return True
        else:
            return False
    return None

def display_result(access, name, n_attempts):

    if access:
        print(f'✅ Access granted. Welcome {name}!')
    else:
        print('❌ Access denied!')
        print(f'{n_attempts} attempts left.')

    if n_attempts == 0:
        print('🚫 Too many attempts. Exiting...')

def main():
    user, password = get_login_input()
    number_of_attempt(check_credentials(user, password))
    display_result(check_credentials(user, password),user, number_of_attempt(check_credentials(user,password)))



main()
