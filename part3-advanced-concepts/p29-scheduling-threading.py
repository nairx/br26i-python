from threading import Timer

def my_task():
    print("Task Executed")

timer = Timer(10,my_task)
timer.start()
# timer.cancel()
print("Timer Started")