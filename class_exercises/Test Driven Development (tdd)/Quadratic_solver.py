import math


def solve_quadratic(a,b,c):
    if a == 0 and b == 0:
        negEquation = ":("
        if c == 0:
            posEquation = "Infinite"
        else:
            posEquation = "Impossible"

    elif a == 0:
        posEquation = (-b + math.sqrt(b*b - 4*a*c))
        negEquation = (-b - math.sqrt(b*b - 4*a*c))
    else:
        posEquation = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
        negEquation = (-b - math.sqrt(b*b - 4*a*c))/(2*a)

    print(posEquation,negEquation) #check during testing for approx
    return posEquation,negEquation
