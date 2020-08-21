"""

This is a minimal python file with a test.

pytest .

"""


def maximum(l: list):
    """Fix this test, eg. using
        return max()

        :param l - a list of numbers
        :return the maximum number in the list

        @solution
    """
    m = l[0]
    for x in l[1:]:
        if x > m:
            m = x
    return m


def test_one():
    """This is a nice test"""
    case = [4, 3, 2, 1, 0]
    expected = 4
    assert maximum(case) == expected
