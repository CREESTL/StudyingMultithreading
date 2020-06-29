import threading
import time


def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += 1
    results.append(result)

results = []


task1 = threading.Thread(
    target=handler,
    kwargs={"finished":2 ** 12} # в первом потоке ищем сумму от 0 до 2^12
)

task2 = threading.Thread(
    target=handler,
    kwargs={"started":2 ** 12, "finished": 2**24} # во втором потоке ищем суммы чисел от 2^12 до 2^24
)

started_at = time.time()

task1.start()
task2.start()

task1.join()
task2.join()

'''
Результаты работы двух потоков
'''
print("TRY 1")
print(f"time: {time.time() - started_at}")
print(f"result: {sum(results)}")

results = []
started_at = time.time()
handler(finished=2**24) # основном потоке считается сумма одного большого отрезка от 0 до 2^24
'''
Результаты обычной работы функции
'''
print("TRY 2")
print(f"time: {time.time() - started_at}")
print(f"result: {sum(results)}")

'''
Казалось бы, что первые два потока должны работать быстрее. То есть первый считает сумму от 0 до 2 в 12, второй - от
2 в 12 до 2 в 24, затем они складываются. И все это происходит параллельно
А основной поток считает весь отрезок от 0 до 2 в 24 водиночку.
Но по факту различия во времени незначительные - все это из-за GIL
'''