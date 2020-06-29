import threading
import time

'''
Здесь рассматривается механизм Producer - Consumer
То есть один поток ожидает события, которые вызывается другим потоком
'''

def producer():
    time.sleep(5)
    print("producer: Releasing the product...")
    '''
    Метод set() уведомляет о том, что событие произошло
    '''
    product.set()
    '''
    Метод clear() говорит о том, что мы очищаем событие и его снова нужно ждать
    '''
    product.clear()

def consumer():
    print("consumer: Waiting for product...")
    '''
    Метод wait() ожидает событие
    Если мы сначала вызовем метод wait() то питон заблокируется и Product exists не выведется на экран до тех пор,
    пока какой-то из потоков не вызовет метод set()
    '''
    product.wait()
    print("consumer: Got it!")


product = threading.Event()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=consumer)

task1.start()
task2.start()

task1.join()
task2.join()

'''
То есть сначала consumer ждет продукта. Через 10 секунд producer создает продукт через set() и consumer егь видит
'''