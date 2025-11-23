import unittest
import random
from src.math_utils import factorial, factorial_recursive, fibo, fibo_recursive
from src.structures import Stack, Queue
from src.sorts import (
    bubble_sort, quick_sort, counting_sort,
    radix_sort, bucket_sort, heap_sort
)


class TestMathAlgos(unittest.TestCase):
    """Тестирование математических функций"""

    def test_factorial(self):
        # Обычные случаи
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        # Ошибка при отрицательных
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_recursive(self):
        self.assertEqual(factorial_recursive(0), 1)
        self.assertEqual(factorial_recursive(5), 120)
        with self.assertRaises(ValueError):
            factorial_recursive(-5)

    def test_fibo(self):
        # Последовательность: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
        self.assertEqual(fibo(0), 0)
        self.assertEqual(fibo(1), 1)
        self.assertEqual(fibo(2), 1)
        self.assertEqual(fibo(10), 55)
        with self.assertRaises(ValueError):
            fibo(-1)

    def test_fibo_recursive(self):
        self.assertEqual(fibo_recursive(0), 0)
        self.assertEqual(fibo_recursive(6), 8)  # 0,1,1,2,3,5,8
        with self.assertRaises(ValueError):
            fibo_recursive(-1)


class TestStructures(unittest.TestCase):
    """Тестирование структур данных (Stack, Queue)"""

    def test_stack_push_pop(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(10)
        s.push(20)
        self.assertEqual(len(s), 2)
        self.assertEqual(s.peek(), 20)
        self.assertEqual(s.pop(), 20)
        self.assertEqual(s.pop(), 10)
        self.assertTrue(s.is_empty())

    def test_stack_min(self):
        """Тест ключевой фичи Medium уровня: min за O(1)"""
        s = Stack()
        s.push(10)
        self.assertEqual(s.min(), 10)
        s.push(5)
        self.assertEqual(s.min(), 5)  # 5 < 10
        s.push(20)
        self.assertEqual(s.min(), 5)  # 20 > 5, минимум все еще 5
        s.push(2)
        self.assertEqual(s.min(), 2)  # 2 < 5

        # Проверяем откат минимума при удалении
        s.pop()  # убрали 2
        self.assertEqual(s.min(), 5)
        s.pop()  # убрали 20
        self.assertEqual(s.min(), 5)
        s.pop()  # убрали 5
        self.assertEqual(s.min(), 10)

    def test_stack_errors(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()
        with self.assertRaises(IndexError):
            s.peek()
        with self.assertRaises(IndexError):
            s.min()

    def test_queue(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(len(q), 3)
        self.assertEqual(q.front(), 1)

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.front(), 2)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertTrue(q.is_empty())

    def test_queue_errors(self):
        q = Queue()
        with self.assertRaises(IndexError):
            q.dequeue()
        with self.assertRaises(IndexError):
            q.front()


class TestSorts(unittest.TestCase):
    """Тестирование алгоритмов сортировки"""

    def setUp(self):
        # Данные для тестов генерируются перед каждым тестом
        self.random_arr = [random.randint(-100, 100) for _ in range(50)]
        self.sorted_arr = list(range(20))
        self.reverse_arr = list(range(20, 0, -1))
        self.empty_arr = []
        self.duplicates_arr = [5, 1, 5, 2, 1, 5]
        self.float_arr = [random.uniform(0, 1) for _ in range(20)]

    def _check_sort(self, sort_func, data, **kwargs):
        """Универсальная проверка: результат функции == sorted(data)"""
        # Важно: передаем копию, чтобы не портить self.data для других проверок
        result = sort_func(data, **kwargs)
        expected = sorted(data, **kwargs)
        self.assertEqual(result, expected, f"Failed {sort_func.__name__} with {kwargs}")

    def test_bubble_sort(self):
        self._check_sort(bubble_sort, self.random_arr)
        self._check_sort(bubble_sort, self.empty_arr)
        # Проверка reverse
        self._check_sort(bubble_sort, self.random_arr, reverse=True)

    def test_quick_sort(self):
        self._check_sort(quick_sort, self.random_arr)
        self._check_sort(quick_sort, self.duplicates_arr)
        # Проверка key (сортировка по модулю)
        arr = [-10, 5, -2, 8]
        self._check_sort(quick_sort, arr, key=abs)

    def test_heap_sort(self):
        self._check_sort(heap_sort, self.random_arr)
        self._check_sort(heap_sort, self.reverse_arr)

    def test_counting_sort(self):
        self._check_sort(counting_sort, self.random_arr)  # С отрицательными
        self._check_sort(counting_sort, self.duplicates_arr)

    def test_radix_sort(self):
        # Radix работает только с неотрицательными числами
        pos_arr = [abs(x) for x in self.random_arr]
        self._check_sort(radix_sort, pos_arr)

        # Проверка на выброс исключения при отрицательных
        with self.assertRaises(ValueError):
            radix_sort([-1, 5, 2])

    def test_bucket_sort(self):
        # Bucket sort хорошо работает с float
        self._check_sort(bucket_sort, self.float_arr)
        # И с int тоже должен работать
        self._check_sort(bucket_sort, [1, 10, 5, 3])


if __name__ == "__main__":
    unittest.main()