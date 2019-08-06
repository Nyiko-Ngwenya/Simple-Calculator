from Calculator import addition,multiply

def test_addition():
    assert addition(3,3) == 6
    assert addition(3, 3,3) == 9
    assert addition(3, 3,3,3) == 12


def test_multiplyy():
    assert multiply(3,3) == 9
    assert multiply(3,2,3) == 18
    assert multiply(3,5,9,7) == 945