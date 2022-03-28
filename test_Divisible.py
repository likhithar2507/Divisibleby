import Divisible

def test_divisible_5():
    num=25
    result=Divisible.divisible_5(num)
    assert result == True

def test_divisible_7():
    num=88
    result=Divisible.divisible_7(num)
    assert result == False

def test_divisible_9():
    num=97
    result=Divisible.divisible_9(num)
    assert result == True

def test_divisible_10():
    num=80
    result=Divisible.divisible_10(num)
    assert result == False
