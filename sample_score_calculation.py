# Sample Score Calculation

def get_student_name():
    name = input("Full name: ")
    return name

def get_score():
    s1 = int(input("Enter first_score: "))
    s2 = int(input("Enter second score: "))
    return s1,s2

def print_result(name,s1,s2):
    t_score = s1 + s2
    avg_s = (t_score / 2)

    print(f"{name}, your total score is {t_score}, and your average is {avg_s}")

    if avg_s > 75:
        print("Passed!")
    else:
        print("Failed!")


def main():
    student_name = get_student_name()
    s1,s2 = get_score()
    print_result(student_name,s1,s2)

main()

