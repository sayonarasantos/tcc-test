import numpy
import os
import time


DIR = "/home/cadmin/manifests"
APP = "mosquitto"


for replicas in [1, 5, 10, 20, 40]:
    TIMES = list()

    for x in range(33):
        start_time = time.time()
        os.system(f"kubectl create -f {DIR}/{APP}.yaml")
        os.system(f"kubectl scale deployment.v1.apps/{APP}-deployment --replicas={replicas}")
        end_time = time.time()

        TIMES.append(end_time - start_time)

        os.system(f"kubectl delete -f {DIR}/{APP}.yaml")

        time.sleep(2)

    with open(f"log-{APP}-deployment-{replicas}.txt", "a") as f:
        f.write(f"# replicas: {replicas}\n")
        for elapsed in TIMES:
            f.write(f"{elapsed}\n")
        f.write(f"\n# entries: {len(TIMES)}\n")
        f.write(f"\n# time mean: {numpy.mean(TIMES)/60}\n")
        f.write(f"\n# time std: {numpy.std(TIMES)/60}\n")
        f.write(f"\n# time var: {numpy.var(TIMES)/60}\n")
