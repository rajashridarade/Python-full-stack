import time
import threading


def display_1():
    data = "111111"
    for ch in data:
        print(ch, end="")
        time.sleep(1)


def display_2():
    data = "222222"
    for ch in data:
        print(ch, end="")
        time.sleep(1)


if __name__ == "__main__":
    thred1 = threading.Thread(name = 'Thred 1',target=display_1)
    thred2 = threading.Thread(name = 'Thred 2',target=display_2)

    thred1.start()
    thred2.start()

