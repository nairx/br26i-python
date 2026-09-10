# import time
# def download_file(name):
#     print(f"Starting {name}")
#     time.sleep(3)
#     print(f"Finished {name}")
# start = time.time()
# download_file("File1.txt")
# download_file("File2.txt")
# download_file("File3.txt")
# print(f"All downloads completed in {time.time()-start:.0f} seconds")

# from threading import *
# import os
# import time
# def download_file(name):
#     print("Child Process",os.getpid())
#     # print(current_thread().name)
#     print(f"Starting {name}")
#     time.sleep(3)
#     print(f"Finished {name}")
# start = time.time()
# t1 = Thread(target=download_file,args=("file1.text",),name="Download File - Thead 1")
# t2 = Thread(target=download_file,args=("file2.text",))
# t3 = Thread(target=download_file,args=("file3.text",))
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
# print(f"All downloads completed in {time.time()-start:.0f} seconds")


# import threading
# import time
# def task():
#     time.sleep(3)
# t=threading.Thread(target=task)
# t.start()
# print(t.is_alive())
# t.join()
# print(t.is_alive())
# print("Program Completed")


# GIL = Global Interpretor lock CPYthon

# import threading
# import time
# counter = 0
# def increment():
#     global counter
#     for i in range(1000):
#         counter = counter + 1
# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(counter)


#without lock - issue
# import threading
# import time
# counter = 0
# def increment():
#     global counter
#     for i in range(1000):
#         temp = counter
#         time.sleep(0.00001)
#         counter = temp + 1
# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(counter)


#lock to resolve race condition
# import threading
# import time
# counter = 0
# lock = threading.Lock()
# def increment():
#     global counter
#     for i in range(1000):
#         with lock:
#             temp = counter
#             time.sleep(0.00001)
#             counter = temp + 1
# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(counter)

#without semaphore
# import threading
# import time
# def task(name):
#     print(name,"enterted")
#     time.sleep(3)
#     print(name,"left")
# threads = []
# for i in range(10):
#     t=threading.Thread(target=task,args=(f"Thread-{i}",))
#     threads.append(t)
#     t.start()
# for i in threads:
#     t.join()
# print("Program Completed")


#with semaphore
# import threading
# import time
# semaphore = threading.Semaphore(3)
# def task(name):
#     with semaphore:
#         print(name,"enterted")
#         time.sleep(3)
#         print(name,"left")
# threads = []
# for i in range(10):
#     t=threading.Thread(target=task,args=(f"Thread-{i}",))
#     threads.append(t)
#     t.start()
# for i in threads:
#     t.join()
# print("Program Completed")

import threading
import time

#Daemon Thread Example
# def background_task():
#     while True:
#         print("Running...")
#         time.sleep(1)

# t=threading.Thread(target=background_task,daemon=True)
# t.start()
# time.sleep(9)
# print("Main Program Finished")

# from concurrent.futures import ThreadPoolExecutor
# import time
# def task(number):
#     time.sleep(3)
#     return number*number 
# with ThreadPoolExecutor(max_workers=3) as executor:
#     results = executor.map(task,[1,2,3,4,5,6,7,8,9])
#     for result in results:
#         print(result)


#parallel threads - with random delay
from concurrent.futures import ThreadPoolExecutor
import time
import random
def task(number):
    print(threading.current_thread().name,"Started")
    t = random.randint(1,9)
    time.sleep(t)
    print(threading.current_thread().name,"Completed")
    return number*number 
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task,[1,2,3,4,5,6,7,8,9])
    for result in results:
        print(result)
        print("------------------")