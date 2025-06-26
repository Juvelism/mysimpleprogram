def test1():
    answer = '1'
    answer2 = '2'

    test = input('Enter: ')
    test2 = input('Enter again: ')

    if test == answer and test2 == answer2:
        return True
    else:
        return False

def display():

    attempts = 3
    while attempts > 0:
        test = test1()
        if test:
            print(f'Accepted!')
            break
        else:
            print(f'Denied!')
            attempts -= 1
            print(f'{attempts} attempts left.')


display()
#
# def main():
#
#     display(test1())
#
# main()