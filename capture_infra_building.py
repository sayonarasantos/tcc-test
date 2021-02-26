import numpy
import time
import os


TIMES = list()
DIR = "/home/cadmin/tcc-automation"


def fprint(msg):
    with open("log-infra-building.txt", "a") as f:
        f.write(f'{msg}\n')


for x in range(2):
    start_time = time.time()
    os.system(f"ansible-playbook {DIR}/build_k3s.yml -i "
              f"{DIR}/inventory/cluster1/hosts.ini")
    os.system(f"ansible-playbook {DIR}/build_management.yml -i "
              f"{DIR}/inventory/cluster1/hosts.ini")
    end_time = time.time()

    time_diff = end_time - start_time
    fprint(f"{time_diff}")
    TIMES.append(time_diff)

    os.system(f"ansible-playbook {DIR}/reset_management.yml -i "
              f"{DIR}/inventory/cluster1/hosts.ini")
    os.system(f"ansible-playbook {DIR}/reset_k3s.yml -i "
              f"{DIR}/inventory/cluster1/hosts.ini")

    time.sleep(60)

fprint(f"\n# entries: {len(TIMES)}")
fprint(f"\n# time mean: {numpy.mean(TIMES)/60}")
fprint(f"\n# time std: {numpy.std(TIMES)/60}")
fprint(f"\n# time variance: {numpy.var(TIMES)/60}")
