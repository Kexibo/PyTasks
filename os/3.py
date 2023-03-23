"""
напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""

import os

list_1 = (os.listdir(r"C:\Users\user\Desktop\папика\os\target"))

for i in list_1:
    if int(i) % 2 == 0:
        os.rename(fr"C:\Users\user\Desktop\папика\os\target\{i}", fr"C:\Users\user\Desktop\папика\os\target\Virus - {i}")
        
