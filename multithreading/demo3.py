import time
import threading


def display(data):
    # data = "111111"
    for ch in data:
        print(ch, end="")
        time.sleep(1)


if __name__ == "__main__":
    thred1 = threading.Thread(name='Thred 1', target=display, args=('1111111',))
    thred2 = threading.Thread(name='Thred 2', target=display, args=('222222',))

    thred1.start()
    thred2.start()
