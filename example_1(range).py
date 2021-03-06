import threading
import time



'''
В других ЯП многопоточность подразумевает, что несколько потоков производят вычисления ПАРАЛЛЕЛЬНО, что очень сильно 
сказывается на скорости. Но в Python есть GIL (Global Interpreter Locker). Что он делает. Допустим у нас есть два потока,
в каждои из них по две подзадачи. Сначала запускается первая подзадача первого потока. Она завершается. Потом ЯП переключается
на первую подзадачу второго потока, она завершается. Затем на вторую подзадачу первого потока и т.д. То есть Python лишь
создает видимость многопоточности, одноко GIL позволяет избежать многих ошибок, которые возможно допустить, если неправильно
пользоваться многопоточностью
'''







'''
Эта функция сама по себе выполняется довольно долго, если ввести большие числа
Поэтому попробуем распараллелить задачи и посмотреть на скорость работы
'''
def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += 1
    print(f"Result is: {result}")

# это фактически число 2 в 26, то есть ищется сумма чисел от 0 до 2 в 26
params = {"finished":2 ** 26}

'''
Создается поток , в аргументы помещаем определенную ранее функцию
'''
task = threading.Thread(target=handler, kwargs=params) # можно писать args или kwags - не важно
started_at = time.time()
print("TRY 1")
'''
Поток запускается (начинает работать функция handler)
'''
task.start()
'''
join() приостанавливает все вычисления, блокируя интерпретатор, пока тело функции handler не закончит выполняться
После этого интерпретатор опять разблокируется и следующие строки кода будут выполняться 
join() присоединяет созданный нами поток к основному потоку интерпретатора
'''
task.join()
print(f"time: {time.time() - started_at}")

'''
Здесь та же самая функция выполнятся в основном потоке, как в обычной программе python
'''
started_at = time.time()
print("TRY 2")
handler(**params)
print(f"time: {time.time() - started_at}")