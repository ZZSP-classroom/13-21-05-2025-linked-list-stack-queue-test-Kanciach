import unittest
from text_editor_2 import *

class TestTextEditor(unittest.TestCase):
    def test_push_and_peek(self):
        stack1 = Stack()
        stack1.push("type 'Sigma'")
        stack1.push("delete 'a'")
        self.assertEqual(stack1.peek(), "delete 'a'")

    def test_pop(self):
        stack1 = Stack()
        stack1.push("type 'Sigma'")
        stack1.push("delete 'a'")
        last_action = stack1.pop()
        self.assertEqual(last_action, "delete 'a'")
        self.assertEqual(stack1.peek(), "type 'Sigma'")

if __name__ == "__main__":
    unittest.main()