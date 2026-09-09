# from multiprocessing import Process 
# import os 
# from time import sleep 

# def calculate(number):
#     print("Child PID:",os.getpid())
#     sleep(30)

# if __name__=="__main__":
#     print("Main Process",os.getpid())
#     p1=Process(target=calculate,args=(1_000_000_0,))
#     p1.start()
#     p1.join()


# from multiprocessing import Process 
# import os 
# from time import sleep 

# def calculate(number):
#     print("Child PID:",os.getpid())
#     sum=0
#     for i in range(number):
#         sum += i
#     print(sum)

# if __name__=="__main__":
#     print("Main Process",os.getpid())
#     p1=Process(target=calculate,args=(1_000_000_0,))
#     p1.start()
#     p1.join()


# from multiprocessing import Process 
# import os 
# from time import sleep 
# def calculate(number):
#     print("Child PID:",os.getpid())
#     sleep(30)
#     # sum=0
#     # for i in range(number):
#     #     sum += i
#     # print(sum)
# if __name__=="__main__":
#     print("Main Process",os.getpid())
#     p1=Process(target=calculate,args=(1_000_000_00,))
#     p2=Process(target=calculate,args=(1_000_000_00,))
#     p3=Process(target=calculate,args=(1_000_000_00,))
#     p1.start()
#     p2.start()
#     p3.start()
#     p1.join()
#     p2.join()
#     p3.join()


#share variable
# from multiprocessing import Process, Value 
# import os 
# from time import sleep 
# def update(counter):
#     counter.value += 1
# if __name__=="__main__":
#     counter = Value('i',0)
#     p1=Process(target=update,args=(counter,))
#     p2=Process(target=update,args=(counter,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("Final:",counter.value)




# PREVENT LOCK variable and race condition
# from multiprocessing import Process, Value,Lock 
# import os 
# from time import sleep 
# def update(counter,lock):
#     for i in range(10000):
#         with lock:
#             counter.value += 1

# if __name__=="__main__":
#     counter = Value('i',0)
#     lock = Lock()
#     p1=Process(target=update,args=(counter,lock))
#     p2=Process(target=update,args=(counter,lock))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("Final:",counter.value)


from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n*n

if __name__=="__main__":
    with ProcessPoolExecutor() as executor:
        results = executor.map(square,[1,2,3,4,5])
        for result in results:
            print(result)
