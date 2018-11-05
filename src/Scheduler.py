# c1 - kara za wczesne
# c2 - kara za późne
# d = podłoga[SUM_P * h]
# F h d [id ' ']+
import math

def schedule(problem, h = 0.8, mode = "default"):
    result = []
    for instance in problem:
        sch_time = 0.0 # czas algorytmu
        F = 0 # funkcja kosztu
        r = 0 # przesunięcie
        SUM_P = sum(job.time for job in instance) # suma czasów zadań
        d = math.floor(SUM_P * h)  # moment rozpoczęcia
        if mode == "sort":
            # wstępne sortowanie
            instance = sortJobs(instance, d)

            # manipulacja czasem startu
            t_temp = 0
            p = 0.1  # procent zadań na krawędziach (czas wykonania)
            left = [] # zadania na lewej krawędzi
            right = [] # zadanie na prawej krawędzi

            for job in instance:
                if (t_temp + job.time < p * SUM_P) or (len(left) == 0):
                    left.append(job)

            for job in reversed(instance):
                if (t_temp + job.time < p * SUM_P) or (len(right) == 0):
                    right.append(job)

            r = (sum(job.c1 for job in left) - sum(job.c2 for job in right)) / (sum(job.c1 for job in left) + sum(job.c2 for job in right))
            # print("SUM_P={} \t r={}".format(SUM_P, r))
            r = 0 if r < 0 else int(r/2 * SUM_P)

            # ostateczne sortowanie
            instance = sortJobs(instance, d)

        t = r
        for job in instance:
            t += job.time
            if t <= d:
                F += job.c1 * math.fabs(d - t)
                # print("before {} {} {}".format(job.c1, job.c2, math.fabs(d - t)))
            if t > d:
                F += job.c2 * math.fabs(d - t)
                # print("after {} {} {}".format(job.c1, job.c2, math.fabs(d - t)))
        # print("\n")
            # print("id={} time={} c1={} c2={}".format(job.id, job.time, job.c1, job.c2))
        result.append((F, h, d, sch_time, instance))
    return result

def sortJobs(instance, d):
    inst_temp = []
    inst_temp2 = []
    t_temp = 0
    # print(d)
    instance = sorted(instance, key=lambda job: job.c1)
    for job in instance:
        t_temp += job.time
        if t_temp < d:
            # print("b {}".format(t_temp))
            inst_temp.append(job)
        else:
            # print("a {}".format(t_temp))
            inst_temp2.append(job)
        inst_temp2 = sorted(inst_temp2, key=lambda job: job.c2, reverse=True)
    instance = inst_temp + inst_temp2
    return instance


