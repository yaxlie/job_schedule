# [a, c1, c2]
# a - czas
# c1 - kara za zbyt wczesne przybycie
# c2 - kara za zbyt późne przybycie
from src.Job import Job


def load(filename):
    file = open(filename, 'r')
    instanceArray = []
    k = file.readline()
    for line in file:
        jobArray = []
        for i in range(0, int(line)):
            element = file.readline()
            temp = ([int(n) for n in element.split()])
            jobArray.append(Job(i, temp[0], temp[1], temp[2]))
        instanceArray.append(jobArray)
    return instanceArray

