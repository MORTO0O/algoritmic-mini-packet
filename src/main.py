import sys
from math_utils import factorial, factorial_recursive, fibo, fibo_recursive
from structures import Stack, Queue
from generators import rand_int_array, nearly_sorted, reverse_sorted
from benchmark import benchmark_sorts
import sorts


def run_benchmarks():
    """Автоматические тесты и замеры времени."""
    print("\n=== ЗАПУСК БЕНЧМАРКОВ ===")

    # 1. Проверка математики
    print("--- Math Check ---")
    print(f"Factorial(5): {factorial(5)}")
    print(f"Fibo(10): {fibo(10)}")
    print()

    # 2. Проверка структур данных
    print("--- Stack Check ---")
    s = Stack()
    s.push(10)
    s.push(5)
    s.push(20)
    print(f"Stack min: {s.min()}")
    print(f"Pop: {s.pop()}")
    print(f"Stack min after pop: {s.min()}")
    print()

    # 3. Бенчмарк сортировок
    print("--- Sorting Benchmarks ---")
    arrays = {
        "random_1000": rand_int_array(1000, 0, 10000),
        "nearly_sorted_1000": nearly_sorted(1000, 10),
        "reverse_1000": reverse_sorted(1000)
    }

    algos = {
        "Bubble": sorts.bubble_sort,
        "Quick": sorts.quick_sort,
        "Heap": sorts.heap_sort,
        "Radix": sorts.radix_sort
    }

    results = benchmark_sorts(arrays, algos)

    for arr_name, res in results.items():
        print(f"\nDataset: {arr_name}")
        for algo_name, t in res.items():
            print(f"  {algo_name}: {t:.6f} sec")

    input("\nНажмите Enter, чтобы вернуться в меню...")


def get_int_input(prompt):
    """Безопасный ввод целого числа."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Введите целое число.")


def get_list_input():
    """Ввод списка чисел через пробел."""
    while True:
        try:
            raw = input("Введите числа через пробел: ")
            parts = raw.strip().split()
            if not parts:
                return []
            # Попытка преобразовать в int, если не вышло - во float
            try:
                return [int(x) for x in parts]
            except ValueError:
                return [float(x) for x in parts]
        except ValueError:
            print("Ошибка: Некорректные данные. Попробуйте снова.")


def interactive_math():
    """Меню математических функций."""
    while True:
        print("\n--- МАТЕМАТИКА ---")
        print("1. Факториал (Итеративно)")
        print("2. Факториал (Рекурсивно)")
        print("3. Фибоначчи (Итеративно)")
        print("4. Фибоначчи (Рекурсивно)")
        print("0. Назад")

        choice = input("Ваш выбор: ")

        if choice == '0':
            break

        if choice in ('1', '2', '3', '4'):
            n = get_int_input("Введите N: ")
            try:
                if choice == '1':
                    print(f"Factorial({n}) = {factorial(n)}")
                elif choice == '2':
                    print(f"Factorial_rec({n}) = {factorial_recursive(n)}")
                elif choice == '3':
                    print(f"Fibo({n}) = {fibo(n)}")
                elif choice == '4':
                    print(f"Fibo_rec({n}) = {fibo_recursive(n)}")
            except ValueError as e:
                print(f"Ошибка вычисления: {e}")
            except RecursionError:
                print("Ошибка: Слишком большая глубина рекурсии.")
        else:
            print("Неверный выбор.")


def interactive_sorts():
    """Меню сортировок."""
    while True:
        print("\n--- СОРТИРОВКИ ---")
        print("1. Bubble Sort")
        print("2. Quick Sort")
        print("3. Counting Sort (только int)")
        print("4. Radix Sort (только int >= 0)")
        print("5. Bucket Sort")
        print("6. Heap Sort")
        print("0. Назад")

        choice = input("Ваш выбор: ")
        if choice == '0':
            break

        algo_map = {
            '1': sorts.bubble_sort,
            '2': sorts.quick_sort,
            '3': sorts.counting_sort,
            '4': sorts.radix_sort,
            '5': sorts.bucket_sort,
            '6': sorts.heap_sort
        }

        if choice in algo_map:
            arr = get_list_input()
            print(f"Исходный массив: {arr}")

            # Дополнительные параметры
            reverse_in = input("Обратный порядок (y/n)? ").lower() == 'y'

            try:
                # Специальная проверка для Radix, так как он капризный
                if choice == '4':
                    if any(x < 0 for x in arr):
                        print("Ошибка: Radix Sort не работает с отрицательными числами.")
                        continue
                    if any(isinstance(x, float) for x in arr):
                        print("Ошибка: Radix Sort работает только с целыми числами.")
                        continue

                # Специальная проверка для Counting, если пользователь ввел float
                if choice == '3' and any(isinstance(x, float) for x in arr):
                    print("Ошибка: Counting Sort работает только с целыми числами.")
                    continue

                # Запуск сортировки
                algo = algo_map[choice]
                sorted_arr = algo(arr, reverse=reverse_in)
                print(f"Результат: {sorted_arr}")

            except Exception as e:
                print(f"Произошла ошибка при сортировке: {e}")
        else:
            print("Неверный алгоритм.")


def interactive_structures():
    """Меню структур данных."""
    while True:
        print("\n--- СТРУКТУРЫ ДАННЫХ ---")
        print("1. Работа со Стеком (Stack)")
        print("2. Работа с Очередью (Queue)")
        print("0. Назад")

        choice = input("Ваш выбор: ")
        if choice == '0':
            break

        if choice == '1':
            s = Stack()
            while True:
                print(f"\n[Stack] Размер: {len(s)}")
                print("1. Push (Добавить)")
                print("2. Pop (Удалить)")
                print("3. Peek (Посмотреть верхний)")
                print("4. Min (Минимум)")
                print("0. Назад")
                act = input("> ")
                try:
                    if act == '1':
                        val = get_int_input("Значение: ")
                        s.push(val)
                        print("Добавлено.")
                    elif act == '2':
                        print(f"Удалено: {s.pop()}")
                    elif act == '3':
                        print(f"Вершина: {s.peek()}")
                    elif act == '4':
                        print(f"Минимум: {s.min()}")
                    elif act == '0':
                        break
                except IndexError as e:
                    print(f"Ошибка: {e}")

        elif choice == '2':
            q = Queue()
            while True:
                print(f"\n[Queue] Размер: {len(q)}")
                print("1. Enqueue (Добавить)")
                print("2. Dequeue (Удалить)")
                print("3. Front (Первый)")
                print("0. Назад")
                act = input("> ")
                try:
                    if act == '1':
                        val = get_int_input("Значение: ")
                        q.enqueue(val)
                        print("Добавлено.")
                    elif act == '2':
                        print(f"Удалено: {q.dequeue()}")
                    elif act == '3':
                        print(f"Первый: {q.front()}")
                    elif act == '0':
                        break
                except IndexError as e:
                    print(f"Ошибка: {e}")


def main():
    """Главное меню программы."""
    while True:
        print("1. Интерактивный режим: Математика")
        print("2. Интерактивный режим: Сортировки")
        print("3. Интерактивный режим: Структуры данных")
        print("4. Автоматический режим (Бенчмарки)")
        print("0. Выход")

        choice = input("\nВыберите режим: ")

        if choice == '1':
            interactive_math()
        elif choice == '2':
            interactive_sorts()
        elif choice == '3':
            interactive_structures()
        elif choice == '4':
            run_benchmarks()
        elif choice == '0':
            print("Выход завершен.")
            sys.exit(0)
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()