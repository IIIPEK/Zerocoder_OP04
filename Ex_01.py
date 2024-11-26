from inputs import input_int

def sum_range(start, end):
    """
    Calculates the sum of all numbers in the given range, inclusive.

    Parameters
    ----------
    start : int
        The start of the range (inclusive).
    end : int
        The end of the range (inclusive).

    Returns
    -------
    int
        The sum of all numbers in the given range.
    """
    summa = 0
    for i in range(start, end + 1):
        summa += i
    return summa


start = input_int("Введите начало диапазона: ")
end = input_int("Введите конец диапазона: ")

print(sum_range(start, end))
