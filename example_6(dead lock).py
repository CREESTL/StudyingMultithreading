import threading

'''
Здесь рассматривается пример блокировки одного потока. То есть он захватывает все выполнение работы, выполняет весь
свой код, затем отдает возможность работать другим потокам
'''

def producer():
    print("Set locking...")
    with lock:
        print('Done!')
        with lock:# поток НЕ МОЖЕТ захватить блокировку, которую он уже захватил
            print('Here is a Dead Lock')
    print("locker released")

lock = threading.Lock()
'''
У Lock() есть два метода, которые вызываются при with lock (см.сверху)
То есть если мы используем with lock то вручную не надо вызывать acquire() и release()
1) __enter__ -> Вызывается функция Lock().acquire()
2) __exit__ -> Вызывается функция Lock().release()
acquire() передает управление программой данному потоку, блокируя остальные
release() дает возможность другим потокам приступить к работе
'''

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()