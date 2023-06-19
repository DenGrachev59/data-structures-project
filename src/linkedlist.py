class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, next_node, data):
        self.next_node = next_node
        self.data = data


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        """Конструктор класса Queue"""
        self.head: None | Node = None
        self.tail: None | Node = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if not self.head and not self.tail:
            self.head = Node(None, data)
            self.tail = Node(None, data)
        elif self.head and self.tail:
            self.head = Node(self.head, data)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if not self.head and not self.tail:
            self.head = Node(None, data)
            self.tail = Node(None, data)
        elif self.head and self.tail:
            new_node = Node(None, data)
            node = self.head
            while node:
                if node.next_node is None:
                    node.next_node = new_node
                    self.tail = new_node
                    break
                node = node.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string