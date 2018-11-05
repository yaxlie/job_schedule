# c1 - kara za wczesne
# c2 - kara za późne
# d = podłoga[SUM_P * h]
# F h d [id ' ']+
import math

def schedule(problem, h = 0.8, mode = "default"):
    result = []
    for instance in problem:
        sch_time = 0.0 # czas algorytmu
        t = 0 # aktualny czas
        F = 0 # funkcja kosztu
        SUM_P = sum(job.time for job in instance) # suma czasów zadań
        d = math.floor(SUM_P * h)  # moment rozpoczęcia
        if mode == "sort":
            inst_temp = []
            t_temp = 0
            instance = sorted(instance, key=lambda job: job.c2)
            for job in instance:
                if t_temp < d:
                    t_temp += job.time
                    inst_temp.append(job)
                    instance.remove(job)
            instance = sorted(instance, key=lambda job: job.c2, reverse=True)
            instance = inst_temp + instance
        for job in instance:
            if t < d:
                F += job.c1 * math.fabs(d - t)
            t += job.time
            if t > d:
                F += job.c2 * math.fabs(d - t)

            # print("id={} time={} c1={} c2={}".format(job.id, job.time, job.c1, job.c2))
        result.append((F, h, d, sch_time))
    return result


