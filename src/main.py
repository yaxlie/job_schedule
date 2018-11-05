from src import FileLoader
from src import Scheduler
import os
from time import time

def main():
    H = [0.2, 0.4, 0.6, 0.8]
    path = "../res/sch"
    for file in os.listdir(path):
        for h in H:
            print("\n{} h={}".format(file.title(), h))
            problem = FileLoader.load(os.path.join(path, file))
            t0 = time()
            result = Scheduler.schedule(problem, h, "sort")
            t1 = time()
            for k in range(0, len(result)):
                # print("\n{} {} {} [id ' ']\n".format(r[0], r[1], r[2]))
                print("{} {} {}s".format(k, result[k][0], float("{0:.3f}".format(t1 - t0))))
                # for job in result[k][4]:
                #     print("(id={} c1={} c2={} time={})".format(job.id, job.c1, job.c2, job.time))
        print("\n")

main()