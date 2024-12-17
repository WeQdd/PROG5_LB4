import unittest
from gen_fib import my_genn

class TestFibonacciCoroutine(unittest.TestCase):
    def test_fib_1(self):
        gen = my_genn()
        gen.send(5)

    def test_fib_2(self):
        gen = my_genn()
        fib_list = next(gen)
        self.assertEqual(fib_list, [0, 1, 1, 2, 3])

    def test_fib_3(self):
        gen = my_genn()
        gen.send(None) 
        fib_list = gen.send(8) 
        self.assertEqual(fib_list, [0, 1, 1, 2, 3, 5, 8, 13])

if __name__ == '__main__':
    unittest.main()