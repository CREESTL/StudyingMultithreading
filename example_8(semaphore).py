import threading
import time

'''
Симафоры позволяют контролировать число  lock-release
До конца так и не понял их смыслаю...
'''

def producer():
    with lock:
        print(f"Set locking: {lock._value}")
        time.sleep(1)
        print("I'm free!")


'''
Это означает, что только ОДИН поток может выполнить функцию. Фактически, это напоминает обычное синхронное выполнение
'''
max_people = 1
lock = threading.BoundedSemaphore(max_people)

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)
task3 = threading.Thread(target=producer)
task4 = threading.Thread(target=producer)

task1.start()
task2.start()
task3.start()
task4.start()

task1.join()
task2.join()
task3.join()
task4.join()

'''
Внутри себя симафор ведет счетчик того, сколько заблокировано и сколько отпущено.
Если вызвать release() еще раз, то это выдаст ошибку
'''
lock.release()


