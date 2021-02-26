import psutil
from psutil._common import bytes2human
import time


CPU = list()
MEM = list()
MEM_PERCENT = list()
DISK = list()
DISK_PERCENT = list()


start = time.time()

for x in range(33):
    CPU.append(psutil.getloadavg()[1])

    MEM.append(psutil.virtual_memory().used)
    MEM_PERCENT.append(psutil.virtual_memory().used * 100
                / psutil.virtual_memory().total)

    DISK.append(psutil.disk_usage('/').used)
    DISK_PERCENT.append(psutil.disk_usage('/').used * 100
                / psutil.disk_usage('/').total)

    time.sleep(2)

end = time.time()

with open('results-resource-master.txt', 'a') as f:
    f.write('CPU\tMEM\t(%)\tDISK\t(%)\n')
    for i in range(len(CPU)):
        f.write('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(
            CPU[i],
            bytes2human(MEM[i]),
            MEM_PERCENT[i],
            bytes2human(DISK[i]),
            DISK_PERCENT[i]
        ))
    f.write('\n# entries: {0}\n'.format(len(CPU)))
    f.write('Total Amount of Memory: {0}\n'.format(
        bytes2human(psutil.virtual_memory().total)))
    f.write('Total Amount of Disk: {0}\n'.format(
        bytes2human(psutil.disk_usage('/').total)))
    f.write('Elapsed time: {0:.2f}s'.format(end - start))
