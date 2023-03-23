"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""
from queue import Queue
from threading import Thread
from time import sleep


def task1(queue):
    Surname = ''
    sleep(2)
    while Surname != "off":
        Surname = input("Введите фимилию: ")
        queue.put(Surname)
        sleep(2)


def task2(queue):
    while True:
        Surname = queue.get()
        if Surname != "":
            print(f"Cтудент {Surname} отчислен")
        else:
            print("Некого отчислять")
        queue.task_done()
        sleep(1)


def main():
    queue = Queue()
    for i in ["Федотов", "Сеченов"]:
        queue.put(i)

    tasky1 = Thread(target=task1, args=(queue,))
    tasky1.start()

    tasky2 = Thread(target=task2, args=(queue,))
    tasky2.start()


main()
