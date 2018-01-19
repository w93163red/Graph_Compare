import numpy as np
import random

class Greedy(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def UUniFastDiscard(self, n, u, nsets):
        sets = []
        while len(sets) < nsets:
            # Classic UUniFast algorithm:
            utilizations = []
            sumU = u
            for i in range(1, n):
                nextSumU = sumU * random.random() ** (1.0 / (n - i))
                utilizations.append(sumU - nextSumU)
                sumU = nextSumU
            utilizations.append(nextSumU)

            # If no task utilization exceeds 1:
            if not [ut for ut in utilizations if ut > 1]:
                sets.append(utilizations)
        return sets[0]

    def run(self):
        N_TASKS = 10
        N_CORES = 4
        flag = [True for _ in range(N_TASKS)]
        flag[0] = False
        util = self.UUniFastDiscard(10, 3, 1)
        num_tasks = 9

        ans = [ [] for i in range(N_CORES)]
        core = 0
        ans[0].append(0)
        u_sum = util[0]
        while num_tasks > 0 and core != N_CORES:
            min_num = -1
            min_sum = 10000

            for i in range(N_TASKS):
                if flag[i]:
                    if len(ans[core]) == 0:
                        min_num = i
                        break
                    sum = 0
                    t_u = u_sum + util[i]
                    if t_u > 1: continue
                    for j in ans[core]:
                        sum += self.matrix[j][i]
                        if sum < min_sum:
                            min_sum = sum
                            min_num = i
            if min_num == -1:
                core += 1
                u_sum = 0
                continue
            ans[core].append(min_num)
            u_sum += util[min_num]
            flag[min_num] = False
            num_tasks -= 1

        tot_sum = 0
        for ls in ans:
            for i in range(len(ls)):
                for j in range(i+1, len(ls)):
                    tot_sum += self.matrix[i][j]

        return (ans, tot_sum)
