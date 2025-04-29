import unittest
from tree import Tree
from node import Node

class TestTree(unittest.TestCase):
    def test_find_existing(self):
        tree = Tree()
        tree.add(10)
        tree.add(5)
        self.assertIsNotNone(tree.find(5))  # gaseste 

    def test_find_missing(self):
        tree = Tree()
        tree.add(10)
        tree.add(20)
        self.assertIsNone(tree.find(15))  # nu gaseste

if __name__ == '__main__':
    unittest.main()
