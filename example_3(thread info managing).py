import threading

'''
Позволяет вывести на экран количество существующих потоков
'''
print(threading.active_count())

'''
Получаем используемый в данный момент поток
Здесь под капотом запускается функция start()
'''
current = threading.current_thread()
'''
Имя потока
'''
print(current.name)
'''
Узнаем, жив ли поток
'''
print(current.is_alive())

'''
Ранее уже запустили функцию start()
Что произойдет, если еще раз попробуем сделать это?
'''
try:
    current.start()
except RuntimeError as e:
    print("ERROR {error}".format(error=e))\

'''
Изменим название потока
'''
current.name = "2chThread"
print(current.name)

'''
Вывод всех запущенных и живых потоков
'''
print(threading.enumerate())
