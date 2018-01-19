import numpy as np
import pickle

class Brute(object):
    N_CORES = 4
    N_TASKS = 10
    matrix = []

    def __init__(self, matrix):
        self.matrix = matrix
        self.ans = pickle.load(open("brute.p", "rb"))

    def get_fitness(self, chromosome):
        allo = []
        sum = 0
        for _ in range(self.N_CORES):
            allo.append([])
        for i in range(len(chromosome)):
            allo[chromosome[i]].append(i)
        for ls in allo:
            for i in ls:
                for j in ls:
                    if i != j and i > j:
                        sum += self.matrix[i][j]
        return sum

    def run(self):
        matrix = np.random.rand(self.N_TASKS, self.N_TASKS)
        for i in range(self.N_TASKS):
            for j in range(self.N_TASKS):
                if (i == j):
                    matrix[i][j] = 0
                if (i > j):
                    matrix[j][i] = matrix[i][j]
        minsum = 10000
        min_ans = None
        for solution in self.ans:
            suma = self.get_fitness(solution)
            if suma < minsum:
                minsum = suma
                min_ans = solution
        return min_ans, minsum