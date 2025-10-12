import pytest
from class_exercises.TDD.Caesar_cipher import to_shift

normal_data = [("a",1,"b"),
                ("z",2,"b"),
                ("g",-3,"d"),
                ("@",1,"@"),
                (" ",1," "),
                ("a",-53,"z"),
                ("a",54,"c"),
                ("a!",1,"b!"),
               ]

@pytest.mark.parametrize("message,shift,code", normal_data)
def test_normal_data(message,shift,code):
    assert to_shift(message,shift) == code

def test_capital_data():
    assert to_shift("A",1) == "B"
    assert to_shift("Z",2) == "B"

#should've parametized this instead bit late now
#@pytest.mark.parametrize("message,shift,code", normal_data)
def test_erroneous_data_calc_grade():
    #message error
    with pytest.raises(TypeError): #should fail
        to_shift(1,1)
    with pytest.raises(TypeError): #should fail
        to_shift(3.14,1)
    with pytest.raises(TypeError): #should fail
        to_shift(True,1)
    # shift error
    with pytest.raises(TypeError):  # should fail
        to_shift(1, "the cake is a lie")
    with pytest.raises(TypeError):  # should fail
        to_shift(1, 3.14)
    with pytest.raises(TypeError):  # should fail
        to_shift(1, True)