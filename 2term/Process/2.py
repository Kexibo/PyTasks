"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""

import multiprocessing

def s(x, y, z):
    s = (x*z*2) + (y*z*2)
    with open("house.txt", "w") as f:
        f.write(str(s))


def paint():
    with open("house.txt", "r") as f:
        otv = 5 * int(f.read())
    with open("house.txt", "a") as f:    
        f.write('\n'+str(otv))


if __name__=='__main__':
    x, y, z = 1, 2, 3
    p1 = multiprocessing.Process(target=s, args=(x,y,z))
    p2 = multiprocessing.Process(target=paint)
    p1.start()
    p1.join()

    p2.start()
