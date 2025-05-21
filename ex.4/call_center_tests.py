import unittest
from call_center_4 import *

class TestCallCenter(unittest.TestCase):
    def setUp(self):
        self.call1 = Call("123", "12:30")
        self.call2 = Call("321", "24:12")
        self.queue1 = Queue()
        self.stack1 = Stack()

    def test_enqueue_dequeue_queue(self):
        self.queue1.enqueue(self.call1)
        self.queue1.enqueue(self.call2)
        self.assertEqual(self.queue1.peek(), self.call1)
        self.assertEqual(self.queue1.denqueue(), self.call1)
        self.assertEqual(self.queue1.peek(), self.call2)

    def test_stack_push_pop(self):
        self.stack1.push(self.call1)
        self.stack1.push(self.call2)
        self.assertEqual(self.stack1.peek(), self.call2)
        self.assertEqual(self.stack1.pop(), self.call2)
        self.assertEqual(self.stack1.peek(), self.call1)

if __name__ == "__main__":
    unittest.main()