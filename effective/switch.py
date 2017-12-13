# coding: utf-8

def f(x):
    """返回对应的值


        Args:
            x: 所要查找的值




    """

    return {
        0: "You typed zere\n",
        1: "one"

    }.get(x, "other value")



def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

from itertools import islice
print list(islice(fib(), 5))


class Seasons:
    Spring, Sumer, Autumn = range(3)


li = range(10)
for i, v in enumerate(li):
    print i, v

# is 是内存中位置一样，检查同一个对象的
# == 是值一样


def print_prime2(n):
    for i in xrange(2, n):
        for j in xrange(2, i):
            if i % j == 0:
                break
        else:
            print '%d' % i


print_prime2(100)