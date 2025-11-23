import random

def rand_int_array(n, lo, hi, *, distinct=False, seed=None):
    """
    Генерация списка случайных целых чисел.

    :param n: Размер списка.
    :param lo: Нижняя граница значений.
    :param hi: Верхняя граница значений.
    :param distinct: Если True, все числа будут уникальными.
    :param seed: Зерно для воспроизводимости.
    """
    if seed is not None:
        random.seed(seed)
    if distinct:
        if (hi - lo + 1) < n:
            raise ValueError("Not enough distinct values in range")
        return random.sample(range(lo, hi + 1), n)
    return [random.randint(lo, hi) for _ in range(n)]


def nearly_sorted(n, swaps, *, seed=None):
    """
    Генерирует почти отсортированный массив путем перестановки swaps пар.
    """
    if seed is not None:
        random.seed(seed)
    arr = list(range(n))
    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def many_duplicates(n, k_unique=5, *, seed=None):
    """
    Генерирует массив длины n, состоящий всего из k_unique уникальных значений.
    """
    if seed is not None:
        random.seed(seed)
    unique_elements = [random.randint(0, 1000) for _ in range(k_unique)]
    return [random.choice(unique_elements) for _ in range(n)]


def reverse_sorted(n):
    """Генерирует отсортированный в обратном порядке массив."""
    return list(range(n, 0, -1))


def rand_float_array(n, lo=0.0, hi=1.0, *, seed=None):
    """Генерирует список случайных чисел с плавающей точкой."""
    if seed is not None:
        random.seed(seed)
    return [random.uniform(lo, hi) for _ in range(n)]