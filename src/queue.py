class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """

        data_push = Node(data, None)
        if self.head is None:
            self.head = data_push
            self.tail = data_push
        else:
            self.tail.next_node = data_push
            self.tail = data_push

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head:   #
            rem = self.head   #
            self.head = self.head.next_node  #
            return rem.data  #
        return None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not self.head:
            return ''
        cur = self.head
        res = ''
        while cur != self.tail:
            res += cur.data
            res += '\n'
            cur = cur.next_node
        res += cur.data
        return res
