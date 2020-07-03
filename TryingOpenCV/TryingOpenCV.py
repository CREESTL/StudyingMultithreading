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
        self.frame = None

    # Функция запускает поток для получения видео
    def start(self):
        print("starting get_thread")
        get_thread = Thread(target=self.get, args=())
        get_thread.name = "get_thread"
        get_thread.start()
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

    def __init__(self, window_name=None, frame=None):
        self.frame = frame
        self.stopped = False
        self.window_name = window_name

    # Функция запускает поток для вывода видео
    def start(self):
        print("starting show_thread")
        show_thread = Thread(target=self.show, args=())
        show_thread.name = "show_thread"
        show_thread.start()
        return self

    # Функция выводит кадр на экран
    def show(self):
        while not self.stopped:
            if self.frame is not None:
                cv2.imshow(self.window_name, self.frame)
            if cv2.waitKey(1) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True

class FaceDetector():
    """
    Класс служит для распознавания лица
    """
    def __init__(self, frame):
        self.face_cascade = cv2.CascadeClassifier('faces.xml')
        self.stopped = False
        self.frame = frame

    def start(self):
        print("starting detect_thread")
        detect_thread = Thread(target=self.detect_faces, args=())
        detect_thread.name = "detect_thread"
        detect_thread.start()
        return self

    def detect_faces(self):
        while not self.stopped:
            try:
                gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray)
                for (x, y, w, h) in faces:
                    cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            except:
                pass

    def stop(self):
        self.stopped = True

def threadBoth():
    """
    Отдельный поток для считывания видео
    Отдельный поток для вывода видео
    Главный поток нужен для передачи кадра между двумя другими потоками
    """

    video_getter = VideoGet().start()
    video_shower_1 = VideoShow("camera 1", video_getter.frame).start()
    video_shower_2 = VideoShow("camera 2", video_getter.frame).start()
    video_detector = FaceDetector(video_getter.frame).start()

    while True:
        if video_getter.stopped or video_shower_1.stopped or video_shower_2.stopped:
            video_shower_1.stop()
            video_shower_2.stop()
            video_getter.stop()
            video_detector.stop()
            break

        # кадр берется из одного потока
        got_frame = video_getter.frame
        # помещается во второй и обрабатывается
        video_detector.frame = got_frame
        # обработанный кадр помещается в третий поток для вывода
        video_shower_1.frame = video_detector.frame
        video_shower_2.frame = video_detector.frame




threadBoth()