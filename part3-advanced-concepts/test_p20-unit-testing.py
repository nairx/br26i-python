import pytest 

@pytest.mark.parametrize("number,result",[(2,4),(3,9),(4,16)])
def test_square(number,result):
    assert number * number == result