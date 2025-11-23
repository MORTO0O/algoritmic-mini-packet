import time


def timeit_once(func, *args, **kwargs):
    """
    Замеряет время выполнения функции func один раз.

    :return: Время выполнения в секундах (float).
    """
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time


def benchmark_sorts(arrays, algos):
    """
    Запуск переданных алгоритмов на переданных наборах данных.

    :param arrays: Словарь {имя_набора: список_данных}.
    :param algos: Словарь {имя_алгоритма: функция_сортировки}.
    :return: Словарь результатов {имя_набора: {имя_алгоритма: время}}.
             Если произошла ошибка, время = -1.0.
    """
    results = {}
    for arr_name, arr in arrays.items():
        results[arr_name] = {}
        for algo_name, algo in algos.items():
            arr_copy = arr.copy()
            try:
                exec_time = timeit_once(algo, arr_copy)
                results[arr_name][algo_name] = exec_time
            except Exception:
                results[arr_name][algo_name] = -1.0
    return results