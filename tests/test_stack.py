"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src import stack
from src.stack import Node, Stack


class TestDataStructures(unittest.TestCase):
    """Test data structures"""

    def test_class_node(self):
        test_class = Node('test')
        self.assertTrue(test_class)

    def test_class_stak(self):
        stak = Stack()
        self.assertTrue(stack)

    def test_push_stack(self):
        self.top = None
        self.size = 0
        test = Stack.push(self,'test1')
        self.assertTrue(self.top)


if __name__ == '__main__':
    unittest.main()
