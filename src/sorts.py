def bubble_sort(a, key=None, reverse=False):
    """
    Сортировка пузырьком (Bubble Sort).

    :param a: Список для сортировки.
    :param key: Функция-ключ для сравнения элементов (опционально).
    :param reverse: Если True, сортирует в убывающем порядке.
    :return: Новый отсортированный список.
    """
    arr = a.copy()
    key_func = key if key else lambda x: x
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            left = key_func(arr[j])
            right = key_func(arr[j + 1])
            if (left > right) if not reverse else (left < right):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def quick_sort(a, key=None, reverse=False):
    """
    Быстрая сортировка (Quick Sort).
    Использует оптимизацию "медиана трех" для выбора опорного элемента.

    :param a: Список для сортировки.
    :param key: Функция-ключ для сравнения.
    :param reverse: Если True, сортирует по убыванию.
    :return: Новый отсортированный список.
    """
    arr = a.copy()
    if len(arr) <= 1:
        return arr
    key_func = key if key else lambda x: x

    def partition(low, high):
        mid = (low + high) // 2
        l_val = key_func(arr[low])
        m_val = key_func(arr[mid])
        h_val = key_func(arr[high])

        # Медиана трех для выбора pivot
        if l_val > m_val:
            arr[low], arr[mid] = arr[mid], arr[low]
            l_val, m_val = m_val, l_val
        if l_val > h_val:
            arr[low], arr[high] = arr[high], arr[low]
            l_val, h_val = h_val, l_val
        if m_val > h_val:
            arr[mid], arr[high] = arr[high], arr[mid]

        pivot_val = key_func(arr[high])
        i = low - 1

        condition = (lambda x: x <= pivot_val) if not reverse else (lambda x: x >= pivot_val)

        for j in range(low, high):
            if condition(key_func(arr[j])):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            _quick_sort(low, pi - 1)
            _quick_sort(pi + 1, high)

    _quick_sort(0, len(arr) - 1)
    return arr


def counting_sort(a, reverse=False):
    """
    Сортировка подсчетом (Counting Sort).
    Поддерживает отрицательные числа путем сдвига индексов.

    :param a: Список целых чисел.
    :param reverse: Если True, возвращает перевернутый список.
    :return: Новый отсортированный список.
    """
    if not a:
        return []
    min_val = min(a)
    max_val = max(a)
    range_val = max_val - min_val + 1
    count = [0] * range_val
    output = [0] * len(a)

    for number in a:
        count[number - min_val] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(a) - 1, -1, -1):
        output[count[a[i] - min_val] - 1] = a[i]
        count[a[i] - min_val] -= 1

    if reverse:
        output.reverse()
    return output


def counting_sort_for_radix(arr, exp, base):
    """
    Вспомогательная функция для Radix Sort. Сортирует по разряду exp.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * base
    for i in range(n):
        index = (arr[i] // exp) % base
        count[index] += 1
    for i in range(1, base):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % base
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]


def radix_sort(a, base=10, reverse=False):
    """
    Поразрядная сортировка (Radix Sort).
    Работает только с неотрицательными целыми числами.

    :param a: Список неотрицательных целых чисел.
    :param base: Основание системы счисления (по умолчанию 10).
    :param reverse: Если True, возвращает перевернутый список.
    :return: Новый отсортированный список.
    :raises ValueError: Если в списке есть отрицательные числа.
    """
    if not a:
        return []
    if min(a) < 0:
        raise ValueError("Radix sort supports only non-negative integers")

    arr = a.copy()
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp, base)
        exp *= base

    if reverse:
        arr.reverse()
    return arr


def bucket_sort(a, buckets=None, key=None, reverse=False):
    """
    Корзинная сортировка (Bucket Sort).
    Использует Bubble Sort для сортировки внутри корзин.

    :param a: Список чисел.
    :param buckets: Количество карманов (по умолчанию равно длине списка).
    :param key: Функция-ключ.
    :param reverse: Флаг обратной сортировки.
    :return: Новый отсортированный список.
    """
    if not a:
        return []
    key_func = key if key else lambda x: x
    values_for_range = [key_func(x) for x in a] if key else a

    min_val = min(values_for_range)
    max_val = max(values_for_range)
    range_val = max_val - min_val

    if buckets is None:
        buckets = len(a)

    if range_val == 0:
        result = a.copy()
        if reverse:
            result.reverse()
        return result

    buckets_list = [[] for _ in range(buckets)]

    for num in a:
        val = key_func(num)
        normalized = (val - min_val) / range_val
        idx = int(normalized * (buckets - 1))
        buckets_list[idx].append(num)

    sorted_arr = []
    for bucket in buckets_list:
        if bucket:
            sorted_arr.extend(bubble_sort(bucket, key=key, reverse=reverse))

    if reverse:
        sorted_arr.reverse()
    return sorted_arr


def heap_sort(a, key=None, reverse=False):
    """
    Пирамидальная сортировка (Heap Sort).

    :param a: Список для сортировки.
    :param key: Функция-ключ.
    :param reverse: Флаг обратной сортировки.
    :return: Новый отсортированный список.
    """
    key_func = key if key else lambda x: x

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        # Сравнение с учетом ключа и флага reverse
        if l < n:
            if (key_func(arr[l]) > key_func(arr[largest])) if not reverse else (
                    key_func(arr[l]) < key_func(arr[largest])):
                largest = l
        if r < n:
            if (key_func(arr[r]) > key_func(arr[largest])) if not reverse else (
                    key_func(arr[r]) < key_func(arr[largest])):
                largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    arr = a.copy()
    n = len(arr)

    # Построение кучи (max-heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr