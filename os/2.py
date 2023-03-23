"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""

import os

os.mkdir(r"C:\Users\user\Desktop\папика\os\target")
os.chdir(r"C:\Users\user\Desktop\папика\os\target")

for i in range(1, 11):
    os.mkdir(f"{i}")
