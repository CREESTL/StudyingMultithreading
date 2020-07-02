'''
Попробую многопоточность с OpenCV
'''

import cv2
import threading
from threading import Thread


class VideoGet():
    """
       Класс берет фреймы в отдельном потоке
    """

    def __init__(self):
        self.stream = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    # Функция запускает поток для получения видео
    def start(self):
        Thread(target=self.get, args=()).start()
        return self

    # Функция получает кадр видео
    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()

    def stop(self):
        self.stopped = True


class VideoShow():
    """
    Класс показывает кадр в отдельном потоке
    """

    def __init__(self, frame=None):
        self.frame = frame
        self.stopped = False

    # Функция запускает поток для вывода видео
    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    # Функция выводит кадр на экран
    def show(self):
        while not self.stopped:
            cv2.imshow("Video", self.frame)
            if cv2.waitKey(1) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True



def threadBoth():
    """
    Отдельный поток для считывания видео
    Отдельный поток для вывода видео
    Главный поток нужен для передачи кадра между двумя другими потоками
    """

    video_getter = VideoGet().start()
    video_shower = VideoShow(video_getter.frame).start()

    print(f"Threads alive: {threading.active_count()}")
    while True:
        if video_getter.stopped or video_shower.stopped:
            video_shower.stop()
            video_getter.stop()
            break

        # кадр постоянно берется из одного потока и помещается в другой
        frame = video_getter.frame
        video_shower.frame = frame





class CarDetector():
    """
    Класс служит для распознавания авто, пока не используется
    """
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('faces.xml')
    def detect_faces():
        print(f"Threads alive: {threading.active_count()}")
        while True:
            print(f"Thread: {threading.current_thread().name}")
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.imshow('video', frame)
            if cv2.waitKey(33) == ord('q'):
                print("Q pressed")
                break

threadBoth()