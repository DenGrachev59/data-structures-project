"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linkedlist import Node, LinkedList


class TestQueue(unittest.TestCase):

    def test_insert_beginning(self):
        test_ll = LinkedList()
        self.assertEqual(str(test_ll), 'None')
        test_ll.insert_beginning({'id': 0})
        test_ll.insert_beginning({'id': 1})
        test_ll.insert_beginning({'id': 2})
        test_ll.insert_beginning({'id': 3})
        test_ll.insert_beginning({'id': 4})
        self.assertEqual(str(test_ll), "{'id': 4} -> {'id': 3} -> {'id': 2} -> {'id': 1} -> {'id': 0} -> None")

    def test_insert_at_end(self):
        test_ll = LinkedList()
        self.assertEqual(str(test_ll), 'None')
        test_ll.insert_at_end({'id': 0})
        test_ll.insert_at_end({'id': 1})
        test_ll.insert_at_end({'id': 2})
        test_ll.insert_at_end({'id': 3})
        test_ll.insert_at_end({'id': 4})
        self.assertEqual(str(test_ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> {'id': 4} -> None")

    def test_insert_beginning_at_end(self):
        test_ll = LinkedList()
        self.assertEqual(str(test_ll), 'None')
        test_ll.insert_at_end({'id': 0})
        test_ll.insert_beginning({'id': 1})
        test_ll.insert_at_end({'id': 2})
        test_ll.insert_beginning({'id': 3})
        test_ll.insert_at_end({'id': 4})
        self.assertEqual(str(test_ll), "{'id': 3} -> {'id': 1} -> {'id': 0} -> {'id': 2} -> {'id': 4} -> None")
