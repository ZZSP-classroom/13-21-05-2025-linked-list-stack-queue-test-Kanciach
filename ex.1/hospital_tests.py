import unittest
from hospital_1 import *

class TestHospital1(unittest.TestCase):
    def test_enqueue(self):
        queue1 = Queue()

        patient1 = Patient("Szyn", "20:30")
        patient2 = Patient("Szyl", "14:00")

        queue1.enqueue(patient1)
        queue1.enqueue(patient2)

        self.assertEqual(queue1.peek(), patient1)

    def test_dequeue(self):
        queue1 = Queue()

        patient1 = Patient("Szyn", "20:30")
        patient2 = Patient("Szyl", "14:00")

        queue1.enqueue(patient1)
        queue1.enqueue(patient2)

        removed = queue1.dequeue()

        self.assertEqual(removed, patient1)
        self.assertEqual(queue1.peek(), patient2)

if __name__ == "__main__":
    unittest.main()