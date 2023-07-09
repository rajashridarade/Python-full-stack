import threading
import time


class Mythread(threading.Thread):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def display(self):
        for ch in self.data:
            print(ch, end=" ")
            time.sleep(1)

    def run(self):
        self.display()


if __name__ == "__main__":
    t1 = Mythread('1111111111111111')
    t2 = Mythread('22222222222222222')
    t3 = Mythread('333333333333333')
    t1.start()
    t1.join() #join with main till t1 finishes
    t2.start()
    t2.join()
    t3.start()
