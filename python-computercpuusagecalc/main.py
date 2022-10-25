#psutil module

import psutil


CPU = psutil.cpu_count()
print(CPU)
while True:
    cpu_Percent = psutil.cpu_percent(1)
    print(cpu_Percent)