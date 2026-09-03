import schedule 
import time
def my_task():
    print("Task Executed")
def my_task2():
    print("Task2 Executed")
job1 = schedule.every().day.at("15:01").do(my_task)
job2 = schedule.every().day.at("16:01").do(my_task2)
schedule.cancel_job(job1)
# schedule.every(10).seconds.do(my_task) #every().minutes , every().hour, every(1).day
# schedule.clear()
# schedule.every().day.at("13:01").do(my_task)
# schedule.every().thursday.at("15:00").do(my_task)
print(schedule.next_run())

while True:
    schedule.run_pending()
    time.sleep(1)