"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
import time
from threading import Thread

def foo():
    task=input('О чем напомнить? : ')
    tim=int(input('Сколько секунд? : '))
    time.sleep(tim)
    print(task)


th = Thread(target=foo)
th.start()
time.sleep(10)
th.join()
print("программа завершается")