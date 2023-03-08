"""
Напишите скрипт который принимает 2 аргумента - путь и имя папки. И создаем папку по указанному пути.
"""
import os
import sys

path = sys.argv[1]
folder_name = sys.argv[2]

os.makedirs(os.path.join(path, folder_name))
