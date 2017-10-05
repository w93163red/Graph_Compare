import Microbial, Brute, GA, Greedy, graph_partition
import numpy as np
from multiprocessing import Process
from time import clock
CROSS_RATE = 0.5
MUTATION_RATE = 0.05
POP_SIZE = 5000
N_GENERATION = 20
N_TASKS = 10
N_CORES = 4
TIMES = 100

def generate_matrix():
    matrix = np.random.rand(N_TASKS, N_TASKS)
    for i in range(N_TASKS):
        for j in range(N_TASKS):
            if (i == j):
                matrix[i][j] = 0
            if (i > j):
                matrix[j][i] = matrix[i][j]
    return matrix

def ga_thread(matrix):
    file = open("ga.txt", "w")
    filet = open("ga_time.txt", "w")
    for i in range(TIMES):
        start = clock()
        print("ga", i)
        ga = GA.GA(matrix[i])
        best_DNA, ans = ga.run()
        file.write("%f\n" % ans)
        end = clock()
        filet.write("%f\n" % (end - start))

def brute_thread(matrix):
    file = open("brute.txt", "w")
    filet = open("brute_time.txt", "w")
    for i in range(TIMES):
        start = clock()
        print("brute", i)
        brute = Brute.Brute(matrix[i])
        best_DNA, ans = brute.run()
        file.write("%f\n" % ans)
        end = clock()
        filet.write("%f\n" % (end - start))

def greedy_thread(matrix):
    file = open("greedy.txt", "w")
    filet = open("greedy_time.txt", "w")
    for i in range(TIMES):
        start = clock()
        greedy = Greedy.Greedy(matrix[i])
        best_DNA, ans = greedy.run()
        file.write("%f\n" % ans)
        end = clock()
        filet.write("%f\n" % (end - start))


def mga_thread(matrix):
    file = open("mga.txt", "w")
    filet = open("mga_time.txt", "w")
    for i in range(TIMES):
        start = clock()
        print("mga", i)
        mga = Microbial.Microbial_GA(matrix[i])
        best_DNA, ans = mga.run()
        file.write("%f\n" % ans)
        end = clock()
        filet.write("%f\n" % (end - start))

def graph_partition_thread(matrix):
    file = open("graph_partition.txt", "w")
    filet = open("graph_time.txt", "w")
    for i in range(TIMES):
        start = clock()
        print("gp", i)
        gp = graph_partition.Graph(matrix[i])
        best_DNA, ans = gp.run()
        file.write("%f\n" % ans)
        end = clock()
        filet.write("%f\n" % (end - start))

if __name__ == "__main__":

    matrix = []
    for i in range(TIMES):
        matrix.append(generate_matrix())

    ga = Process(target=ga_thread, args=(matrix,))
    greedy = Process(target=greedy_thread, args=(matrix,))
    brute = Process(target=brute_thread, args=(matrix,))
    mga = Process(target=mga_thread, args=(matrix,))
    gp = Process(target=graph_partition_thread, args=(matrix,))
    greedy.start()
    ga.start()
    brute.start()
    mga.start()
    gp.start()

