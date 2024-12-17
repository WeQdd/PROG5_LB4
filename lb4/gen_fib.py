import functools

def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res

g = fib_elem_gen()

while True:
    el = next(g)
    print(el)
    if el > 10:
        break
        
       

def my_genn():
    """Сопрограмма"""
    a, b = 0, 1
    while True:
        n = yield
        if n is None:
            n = 5  # или другое значение по умолчанию
        fib_list = []
        for _ in range(n):
            fib_list.append(a)
            a, b = b, a + b
        yield fib_list


def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


my_genn = fib_coroutine(my_genn)
gen = my_genn()
print(gen.send(5))



class FibonacchiLst:
    def __init__(self, lst):
        self.lst = lst
        self.idx = 0
        self.fib_set = set()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                num = self.lst[self.idx]
                self.idx += 1
            except IndexError:
                raise StopIteration

            if self.is_perfect_square(5 * num * num + 4) or self.is_perfect_square(5 * num * num - 4):
                return num

    def is_perfect_square(self, num):
        s = int(num ** 0.5)
        return s * s == num
    
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
fib_iter = FibonacchiLst(lst)
for num in fib_iter:
    print(num)  