import threading

'''
Если мы работаем с несколькими потоками, то удобно создать безопасное хранилище данных для всех этих потоков.
Суть его в том, что если данные в одном потоке меняются, то они не затрагиваются в другом
То есть для каждого потока создается свое value
Это делается так:
'''

thread_data = threading.local()
thread_data.value = 5 # как бы глобальная переменная

# Функция выводит значения .value потока
# Она будет запускаться в разных потоках, чтобы проверить, чему равняется value каждого потока
def print_value():
    print(threading.current_thread())
    print(f"Result : {thread_data.value}")

# Фунция для КАЖДОГО потока увеличивает атрибут value times раз
def counter(started, times):
    thread_data.value = started # создается уникальный для данного потока value
    for i in range(times):
        thread_data.value += 1
    print_value()

# args передаются в функцию counter
task1 = threading.Thread(target=counter, args=(0, 10), name="task1")
task2 = threading.Thread(target=counter, args=(100, 3), name="task2")

'''
Оба потока работают так, как ожидалось
Выводятся результаты 10 и 103
'''
task1.start()
task2.start()

'''
А теперь выведем результаты в основном потоке
Выводится 5 (в начале кода было задано) - все работает верно
'''
print_value()








