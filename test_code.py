def get_user(user, password):

    admin_credentials = {
        'admin1': 'admin123',
        'admin2': 'admin456',
        'admin3': 'admin789'
    }

    for i in admin_credentials:
        if user == i and password == admin_credentials[i]:
            return True
        else:
            return False
    return None

def display(admin, user):
    if admin:
        print('Success')
    else:
        print("Failed")

    print(f'Welcome {user}')


def main():
    pass

main()


