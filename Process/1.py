"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""
import multiprocessing
def chet(num=1_000_000):
    print(sum([i if i % 2 == 0 else 0 for i in range(1, 1_000_001)]))


def nechet(num=1_000_000):
    print(sum([i if i % 2 != 0 else 0 for i in range(1, 1_000_001)]))

if __name__=='__main__':
    p1 = multiprocessing.Process(target=chet)
    p2 = multiprocessing.Process(target=nechet)

    p1.start()
    p2.start()

    p1.join()
