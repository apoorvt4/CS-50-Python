'''from calculator import square


def main():
    test_square()

def test_square():
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 square is not 4")
    try:
        assert square(3) == 8
    except AssertionError:
        print("3 square is not 8")
    try:
        assert square(50) == 10
    except AssertionError:
        print("50 square is not 10")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 Square is not 50")


 


if __name__=="__main__":
    main()'''

import pytest
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")




