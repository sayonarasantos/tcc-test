import numpy
import os
import time


DIR = "/home/cadmin/k3s_manifests"
APP = "app"


def fprint(msg):
    with open("log-app-deployment.txt", "a") as f:
        f.write(f'{msg}\n')


for replicas in [1, 5, 10]
    print(f"START LOOP WITH {replicas} replicas")

    times_list = list()

    for x in range(3):
        print(f"START DEPLOYMENT")
        start_time = time.time()
        os.system(f"kublectl create -f {DIR}/{APP}-{replicas}.yaml")
        end_time = time.time()
        time_diff = end_time - start_time
        fprint(f"{x} - Diff time: {time_diff}")
        times_list.append(time_diff)
        os.system(f"kublectl delete -f {DIR}/{APP}-{replicas}.yaml")
        time.sleep(2)

    fprint(f"{replicas} - List diff: {times_list}")
    print(f"{replicas} - List dif: {times_list}")

    fprint(f"{replicas} - Time mean: {numpy.mean(times_list)/60}")
    print(f"{replicas} - Time mean: {numpy.mean(times_list)/60}")
