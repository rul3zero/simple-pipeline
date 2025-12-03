import count

def test_add_positive():
    assert count.add(2, 3) == 5

def test_add_negative():
    assert count.add(-1, -1) == -2

def test_subtract():
    assert count.subtract(10, 5) == 5

def test_subtract_negative():   
    assert count.subtract(-1, -1) == 0