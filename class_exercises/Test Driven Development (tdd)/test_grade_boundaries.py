import pytest
import warnings
from class_exercises.tdd.grade_boundaries import calc_grade

min_test_data = [(0,"U"),
             (72,"E"),
             (111,"D"),
             (150,"C"),
             (189,"B"),
             (229,"A"),
             (264,"A*"),
             ]

max_test_data = [(71,"U"),
             (110,"E"),
             (149,"D"),
             (188,"C"),
             (228,"B"),
             (263,"A"),
             (350,"A*"),
             ]

@pytest.mark.parametrize("score,grade", min_test_data) #this tests everything in test_data one by one
def test_min_calc_grade(score, grade):
    assert calc_grade(score) == grade

@pytest.mark.parametrize("score,grade", max_test_data)
def test_max_calc_grade(score, grade):
    assert calc_grade(score) == grade

def test_normal_calc_grade():
    assert calc_grade(259) == "A"
    assert calc_grade(210) == "B"

def test_erroneous_data_calc_grade():
    with pytest.raises(TypeError):
        calc_grade("A")