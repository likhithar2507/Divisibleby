import Divisible
import pytest

@pytest.fixture
def input():
    x=25
    return x

def test_divisible_5(input):

    result=Divisible.divisible_5(input)
    assert result == True

def test_divisible_7(input):

    result=Divisible.divisible_7(input)
    assert result == False

def test_divisible_9(input):

    result=Divisible.divisible_9(input)
    assert result == True

def test_divisible_10(input):

    result=Divisible.divisible_10(input)
    assert result == False






