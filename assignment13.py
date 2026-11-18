
import threading
import time

def task1():
    for i in range(1, 4):
        print("Task 1: Downloading file", i)
        time.sleep(1)

def task2():
    for i in range(1, 4):
        print("Task 2: Sending email", i)
        time.sleep(1)

def task3():
    for i in range(1, 4):
        print("Task 3: Processing data", i)
        time.sleep(1)

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All tasks completed!")
