import threading
from time import sleep


def do_job(number):
    sleep(3)
    print(f"Job {number} finished")


# rewrite everything inside this main function and keep others untouched

def main(i):
    do_job(i)


a = threading.Thread(target=main, args=(0,))
a.start()
b = threading.Thread(target=main, args=(1,))
b.start()
c = threading.Thread(target=main, args=(2,))
c.start()
d = threading.Thread(target=main, args=(3,))
d.start()
e = threading.Thread(target=main, args=(4,))
e.start()
