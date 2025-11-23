class Node:
    """
    Узел односвязного списка.
    Хранит значение, ссылку на следующий элемент и минимум в стеке.
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
        self.min = value
        # Поддержание минимума за O(1)
        if next_node is not None:
            self.min = min(value, next_node.min)

class Stack:
    """
    Стек на основе связного списка.
    """
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, x):
        """Добавляет элемент на вершину стека."""
        self._top = Node(x, self._top)
        self._size += 1

    def pop(self):
        """
        Удаляет и возвращает элемент с вершины стека.
        :raises IndexError: Если стек пуст.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return value

    def peek(self):
        """Возвращает верхний элемент без удаления."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._top.value

    def is_empty(self):
        """Возвращает True, если стек пуст."""
        return self._top is None

    def __len__(self):
        return self._size

    def min(self):
        """
        :raises IndexError: Если стек пуст.
        """
        if self.is_empty():
            raise IndexError("min from empty stack")
        return self._top.min

class Queue:
    """
    Очередь на основе связного списка.
    """
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def enqueue(self, x):
        """Добавляет элемент в конец очереди."""
        new_node = Node(x)
        if self._rear is None:
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1

    def dequeue(self):
        """
        Удаляет и возвращает элемент из начала очереди.
        :raises IndexError: Если очередь пуста.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self._front.value
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return value

    def front(self):
        """Возвращает первый элемент очереди без удаления."""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._front.value

    def is_empty(self):
        return self._front is None

    def __len__(self):
        return self._size