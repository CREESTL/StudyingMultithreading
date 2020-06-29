import threading
import os

'''
Timer() позволяет создать таймер, который каждые N секунд запускает на выполнение поток
'''

''' 
Через 5 секунд вызывается функция hello() в отдельном потоке, который уничтожается после выполнения функции
'''
def exec_watcher():
    timer = threading.Timer(5.0, hello)
    timer.start()


def hello():
    print(f"Threads alive: {threading.active_count()}")
    for i in os.listdir('.'):
        print(i)
    exec_watcher() # если вызвать эту функцию еще раз, то будет КАЖДЫЕ 5 секунд выводиться список файлов

exec_watcher()