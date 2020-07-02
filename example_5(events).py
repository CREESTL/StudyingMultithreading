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
    Метод set() "начинает" событие. И уведомаляет методы wait(), о том, что оно началось
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
    Если мы сначала вызовем метод wait() то интерпретатор заблокируется и Product exists не выведется на экран до тех пор,
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
1) Запускается функция wait()
2) Через 5 секунд запускается функция set()
3) Функция wait() на это реагирует
4) Запускается фукнция clear()
'''