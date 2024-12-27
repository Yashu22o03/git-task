
from main import add

def test_add():
    assert add(2,3) == 5
    print("Assertion passed!")
    assert add(0, 42) == 42
    print("Assertion passed!")
    assert add(-1, 1) == 0
    print("Assertion passed!")
