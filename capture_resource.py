import psutil
from psutil._common import bytes2human
import numpy
import time


CPU = list()
MEM = list()
MEM_PERCENT = list()
DISK = list()
DISK_PERCENT = list()


def fprint(msg):
    with open("log-resource-manager.txt", "a") as f:
        f.write(f'{msg}\n')


for x in range(33):
    CPU.append(psutil.getloadavg()[1])

    MEM.append(psutil.virtual_memory().used)
    MEM_PERCENT.append(psutil.virtual_memory().used * 100
                / psutil.virtual_memory().total)

    DISK.append(psutil.disk_usage('/').used)
    DISK_PERCENT.append(psutil.disk_usage('/').used * 100
                / psutil.disk_usage('/').total)

    time.sleep(2)

with open('log-resource.txt', 'a') as f:
    f.write('CPU\tMEM\t(%)\tDISK\t(%)\n')
    for i in range(len(CPU)):
        f.write(f"{CPU[i]}\t{bytes2human(MEM[i])}\t{MEM_PERCENT[i]}"
                f"\t{bytes2human(DISK[i])}\t{DISK_PERCENT[i]}\n")

    f.write(f"\n# entries: {len(CPU)}\n")

    f.write('metric\tCPU\tMEM\t(%)\tDISK\t(%)\n')

    f.write(f"mean:\t{numpy.mean(CPU)}\t{bytes2human(numpy.mean(MEM))}"
            f"\t{numpy.mean(MEM_PERCENT)}\t{bytes2human(numpy.mean(DISK))}\t{numpy.mean(DISK_PERCENT)}\n")

    f.write(f"std:\t{numpy.std(CPU)}\t{bytes2human(numpy.std(MEM))}"
            f"\t{numpy.std(MEM_PERCENT)}\t{bytes2human(numpy.std(DISK))}\t{numpy.std(DISK_PERCENT)}\n")

    f.write(f"var:\t{numpy.var(CPU)}\t{bytes2human(numpy.var(MEM))}"
            f"\t{numpy.var(MEM_PERCENT)}\t{bytes2human(numpy.var(DISK))}\t{numpy.var(DISK_PERCENT)}\n")
