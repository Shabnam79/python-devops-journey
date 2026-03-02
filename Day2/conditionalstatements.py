cpu_usage = 85
memory_usage = 70
if cpu_usage >= 85 and memory_usage >=70:
   print("Send alert: CPU and Memory usage are high") 
elif cpu_usage <= 80 and memory_usage <= 65:
   print("System is running smoothly") 
else:
   print("Monitor the system closely")    