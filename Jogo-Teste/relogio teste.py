import time
import os

while True:
    os.system('cls')
    print(f'{time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}')
    time.sleep(1)
