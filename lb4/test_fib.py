import unittest
from gen_fib import my_genn

class TestFibonacciCoroutine(unittest.TestCase):
    def test_fib_1(self):
        gen = my_genn()
        gen.send(None)  
        self.assertEqual(gen.send(3), [0, 1, 1])

    def test_fib_2(self):
        gen = my_genn()
        gen.send(None)  #
        self.assertEqual(gen.send(5), [0, 1, 1, 2, 3])

    def test_fib_3(self):
        gen = my_genn()
        gen.send(None)  
        self.assertEqual(gen.send(8), [0, 1, 1, 2, 3, 5, 8, 13])

if __name__ == '__main__':
    unittest.main()