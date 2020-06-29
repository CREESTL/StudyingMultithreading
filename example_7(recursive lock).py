import threading

'''
В этом примере описывается как можно избежать ошибки Dead Lock из примера 6
'''

def producer():
    print("Set locking...")
    with lock:
        print('Done!')
        with lock:# поток МОЖЕТ захватить блокировку, которую он уже захватил
            print('Recursive lock activated')
    print("locker released")

'''
Все различие в том, что вместо Lock() используем RLock()
'''
lock = threading.RLock()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()