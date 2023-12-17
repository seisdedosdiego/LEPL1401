# Diego Seisdedos Stoz
# BARB27 - Equipe 11.74

import unittest
from orderedlinkedlist import OrderedLinkedList

class OrderedLinkedListTest(unittest.TestCase):

    def setUp(self):
        self.lst1 = OrderedLinkedList([1,2,3])
        self.lst2 = OrderedLinkedList(["ba", "ab"])

    def test_init(self):
        self.assertEqual(self.lst1.get_array(), [1,2,3])
        self.assertEqual(self.lst2.get_array(), ["ab", "ba"])

    def test_add(self):
        self.lst1.add(5)
        self.lst1.add(4)
        self.lst1.add(3)
        self.assertEqual([1,2,3,3,4,5], self.lst1.get_array())

    def test_remove(self):
        self.lst1.remove(2)
        self.assertEqual([1,3], self.lst1.get_array())

    def test_search(self):
        self.assertEqual(self.lst1.search(3), (3, 2))

if __name__ == '__main__':
    unittest.main()