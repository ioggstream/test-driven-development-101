#
# This is a minimal python file with a test.
# 
# pytest .
#
def maximum(l: list):
    # fix this test, eg using
    # return max(l)
    raise NotImplementedError

def test_one():
    case = [4, 3, 2, 1, 0]
    expected = 4
    assert maximum(case) == expected
