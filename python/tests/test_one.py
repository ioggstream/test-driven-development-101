from tdd_course.utils import maximum


def test_one():
    case = [4, 3, 2, 1, 0]
    expected = 4
    assert maximum(case) == expected


