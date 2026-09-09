# import os
# print(os.cpu_count())


import os
import psutil 

print(psutil.cpu_count(logical=False))
print(psutil.cpu_count(logical=True))