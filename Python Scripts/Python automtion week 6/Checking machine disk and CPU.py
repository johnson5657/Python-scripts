import shutil
import psutil

du = shutil.disk_usage("C:\\")

print(du)
print("Disk usage is "+ str(du.free/du.total*100) )

#checking CPU load
print(psutil.cpu_percent(0.1))