import time


def display():
    data = "111111"
    for ch in data:
        print(ch, end="")
        time.sleep(1)


if __name__ == "__main__":
    display()
