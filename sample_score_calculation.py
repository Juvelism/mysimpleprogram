# Sample Score Calculation

def get_student():
    name = input("Student name: ")
    return  name

def get_score():
    s1 = int(input("Enter your 1st score: "))
    s2 = int(input("Enter your 2nd score: "))
    return s1,s2

def printing_view(name, s1, s2):
    t_score = s1 + s2
    avg_c = t_score /  2
    marks = ["Passed", "Failed"]

    print(f"Full name: {name}")
    print(f"Total Score: { t_score}")
    print(f"Average: {avg_c}")

    if avg_c > 75:
        print(f"Remarks: {marks[0]}")
    else:
        print(f"Remarks: {marks[1]}")

def main():


main()
