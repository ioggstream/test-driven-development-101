def maximum(numbers: list) -> int:
    """@solution
    """
    m = numbers[0]
    for n in numbers[1:]:
        if n > m:
            m = n
    return m


def get_maximum(body: dict) -> str:
    """@solution"""

    numbers = body["numbers"]
    return {"maximum": maximum(numbers)}


def test_maximum():
    expected, value = 4, [4, 3, 2, 1]
    assert maximum(value) == expected


def test_get_maximum():
    """Write a test function for get_maximum,
        then implement both.

        @solution
    """
    assert get_maximum({"numbers": [4, 3, 2, 1]}) == {"maximum": 4}
