def maximum(numbers):
    m = numbers[0]
    for x in numbers:
        if m < x:
            m = x
    return m

