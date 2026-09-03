from calculator import *
import pytest

def test_add():
    assert add(2,3) == 5

@pytest.mark.skip
def test_multiply():
    assert multiply(2,3) == 6

def test_subtract():
    assert subtract(5,4) == 1

def test_divide():
    assert divide(4,2)==2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)

@pytest.mark.skipif(True,reason="Not ready")
def test_feature():
    pass

@pytest.mark.xfail
def test_bug():
    assert False