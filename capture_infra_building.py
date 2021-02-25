import numpy
import time
import os


TIMES = list()
DIR = "/home/cadmin/tcc-automation"


def fprint(msg):
    with open("log-infra-building.txt", "a") as f:
        f.write(f'{msg}\n')


for x in range(1):
    print(f"START BUILDING")
    start_time = time.time()
    os.system(f"ansible-playbook {DIR}/build_k3s.yml -i "
              f"{DIR}/inventory/cluster1/hosts.ini")
    os.system(f"ansible-playbook {DIR}/build_management.yml -i "
              f"{DIR}/inventory/cluster1/hosts.ini")
    end_time = time.time()
    time_diff = end_time - start_time
    fprint(f"{x} - Diff time: {time_diff}")
    TIMES.append(time_diff)
    os.system(f"ansible-playbook {DIR}/reset_management.yml -i "
              f"{DIR}/inventory/cluster1/hosts.ini")
    os.system(f"ansible-playbook {DIR}/reset_k3s.yml -i "
              f"{DIR}/inventory/cluster1/hosts.ini")
    time.sleep(2)

fprint(f"List diff: {TIMES}")
print(f"List diff: {TIMES}")

fprint(f"Time mean: {numpy.mean(TIMES)/60}")
print(f"Time mean: {numpy.mean(TIMES)/60}")
