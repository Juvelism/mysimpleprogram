# Calculating Grade

def name_of_student():
    name_student = input("Full name: ")
    return name_student

def grade_of_student():
    grade_1 = int(input("Enter grade #1: "))
    grade_2 = int(input("Enter grade #2: "))
    grade_3 = int(input("Enter grade #3: "))
    return grade_1, grade_2, grade_3

def calculation_of_grade(name,g1,g2,g3):
    sum_g = g1 + g2 + g3
    avg_g = sum_g / 3
    print("-" * 10)
    print(f"Student name: {name}")
    print(f"Average: {avg_g:.2f}")

def main():
    s_name = name_of_student()
    g1,g2,g3 = grade_of_student()
    calculation_of_grade(s_name,g1,g2,g3)

main()