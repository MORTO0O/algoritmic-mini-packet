def factorial(n):
    """
        Вычисление факториала числа n рекурсивно.

    :param n: Неотрицательное целое число.
    :return: Факториал числа n.
    :raises ValueError: Если n < 0.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """
    Вычисление факториала числа n рекурсивно.

    :param n: Неотрицательное целое число.
    :return: Факториал числа n.
    :raises ValueError: Если n < 0.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibo(n):
    """
    Вычисление n-ого числа Фибоначчи итеративно.

    :param n: Порядковый номер (неотрицательный).
    :return: n-е число Фибоначчи.
    :raises ValueError: Если n < 0.
    """
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibo_recursive(n):
    """
    Вычисление n-ого числа Фибоначчи рекурсивно.

    :param n: Порядковый номер (неотрицательный).
    :return: n-е число Фибоначчи.
    :raises ValueError: Если n < 0.
    """
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)