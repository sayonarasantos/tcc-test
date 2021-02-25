import psutil
import numpy


CPU = list()
MEM = list()
DISK = list()


def fprint(msg):
    with open("log-resource.txt", "a") as f:
        f.write(f'{msg}\n')


print(f"START LOOP")
for _ in range(3):
    CPU.append(psutil.cpu_percent(interval=1))
    MEM.append(psutil.virtual_memory().used * 100
                / psutil.virtual_memory().total)
    DISK.append(psutil.disk_usage('/').used * 100
                / psutil.disk_usage('/').total)


fprint(f"CPU mean: {numpy.mean(CPU):.2f}")
print(f"CPU mean: {numpy.mean(CPU):.2f}")

fprint(f"MEM mean: {numpy.mean(MEM):.2f}")
print(f"MEM mean: {numpy.mean(MEM):.2f}")

fprint(f"DISK mean: {numpy.mean(DISK):.2f}")
print(f"DISK mean: {numpy.mean(DISK):.2f}")
