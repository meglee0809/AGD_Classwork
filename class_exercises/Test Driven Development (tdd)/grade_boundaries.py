def calc_grade(mark: int)-> str :
    grade = ""
    if mark >= 264:
        grade = "A*"
    elif mark >= 229:
        grade = "A"
    elif mark >= 189:
        grade = "B"
    elif mark >= 150:
        grade = "C"
    elif mark >= 111:
        grade = "D"
    elif mark >= 72:
        grade = "E"
    else:
        grade = "U"

    return grade

#main program -----------------------------------

mark_valid = False

if __name__ == "__main__":
    print(calc_grade(234))

'''
while mark_valid == False:
    user_mark = int(input("Score: "))
    if user_mark >= 0 and user_mark <= 350:
        user_grade = calc_grade(user_mark)
        print(f"Your grade is {user_grade}.")
        mark_valid = True
'''


    