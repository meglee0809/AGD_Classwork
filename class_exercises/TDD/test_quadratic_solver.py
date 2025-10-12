import pytest
from pytest import approx
import math
from class_exercises.TDD.Quadratic_solver import solve_quadratic

normal_data = [(1,-5,6, 3.0,2.0), #integer
                (1,6,5, -5.0,-1.0), #double check
                (2,-3,-2, 2.0,-0.5), #float result
               ]

abnormal_data = [(0,2,-8, 4.0,0), #forms linear equation
                 (1,-4,4, 2,0), #returns one root

                # !! why is this correct when 1 and -1 are not that close? !!
                 (2,0,-2, math.sqrt(2),0), #gives irrational number
                 (1,7,4,approx(-6.3723),approx(-0.6277)), #long float result using approx
                 (0,0,0, "Infinite",":("), #for 0,0,0 which returns infinite
                 (0,0,5, "Impossible",":("),#for 0,0,n that is impossible

                #complex numbers - too complicated so may add after
#                (1,1,1, (-1 + math.sqrt(-3))/2, (-1 - math.sqrt(-3))/2 ), #integer
#                (3.14,6.04,24.6, *insert disgusting number*) #float
                ]


@pytest.mark.parametrize("a,b,c,posAns,negAns", normal_data)
def test_normal_data(a,b,c,posAns,negAns):
    assert solve_quadratic(a,b,c) == (posAns,negAns) or (negAns,posAns)

@pytest.mark.parametrize("a,b,c,posAns,negAns", abnormal_data)
def test_boundary_data(a,b,c,posAns,negAns):
    assert solve_quadratic(a,b,c) == (posAns,negAns) or (negAns,posAns)


#type testing ---------------------------
def test_type_data():
    test_string_type()
    test_boolean_type()

def test_string_type():
    with pytest.raises(TypeError):
        solve_quadratic("string","cheese","cheese string")

def test_boolean_type():
    with pytest.raises(ValueError):
        solve_quadratic(True,False,True) #the cake is a lie?