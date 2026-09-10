# import asyncio
# async def task():
#     print("Task Started")
#     await asyncio.sleep(2) #let another task run when waiting
#     print("Task completed")
# asyncio.run(task())


import time
import asyncio 
async def task(name):
    print(f"{name} started")
    # time.sleep(2)
    await asyncio.sleep(2)
    #await db connection
    print("Task completed")
async def main():
    start = time.time()
    await asyncio.gather(
        task("Task 1"),
        task("Task 2"),
        task("Task 3")
    )
    print(f"Completed in {time.time()-start:.0f} seonds")
asyncio.run(main())