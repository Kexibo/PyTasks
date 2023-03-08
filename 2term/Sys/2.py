"""
Напишите скрипт который получает системный ввод от пользователя и выводит надпись "команда принята" если ввод начинается
с sys.in.
"""
import sys


user_intup = sys.stdin.readline()
if user_intup.startswith("sys.in"):
    print("Команда принята")
