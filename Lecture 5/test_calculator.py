#Run "pip install pytest"
#Run file with "pytest test_calculator.py"
#Method name must start with "test"

import pytest
from calculator import square

def test_zero():
    assert square(0) == 0

def test_positive():
    assert square(2) == 4

def test_negative():
    assert square(-2) == 4

def test_str():
    with pytest.raises(TypeError):
        square("cat")

def test_failure():
    assert square("cat") == 9