"""
Напишите функцию которая через канал обмена возвращает количество валюты которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""

import multiprocessing, time

def pip(conn, val):
    conn.send(int(val)*75)
    conn.close()


if __name__=='__main__':
    val = input('Введите кол-во валюты: ')
    while val != 'off':
        mama_conn, sin_conn = multiprocessing.Pipe()
        p = multiprocessing.Process(target=pip, args=(sin_conn, val))
        
        p.start()
        print(mama_conn.recv())
        p.join()
        val = input('Введите кол-во валюты: ')
