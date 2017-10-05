import numpy as np
import matplotlib.pyplot as plt

brute_file = open("ans/brute.txt", "r")
ga_file = open("ans/ga.txt", "r")
greedy_file = open("ans/greedy.txt", "r")
mga_file = open("ans/mga.txt", "r")
gp_file = open("ans/graph_partition.txt", "r")

brute = []
ga = []
greedy = []
mga = []
gp = []

for i in range(100):
    f = brute_file.readline()
    brute.append(f)
    f = ga_file.readline()
    ga.append(f)
    f = greedy_file.readline()
    greedy.append(f)
    f = mga_file.readline()
    mga.append(f)
    f = gp_file.readline()
    gp.append(f)

x = [i for i in range(100)]
plt.plot(x, brute, label="Brute Force Algorithm", marker='*')
plt.plot(x, ga, label="Genetic Algorithm", marker='*')
plt.plot(x, mga, label="Microbial Genetic Algorithm", marker='*')
plt.plot(x, greedy, label="Greedy Algorithm", marker='*')
plt.plot(x, gp, label="Graph Parition Algorithm", marker='*')
plt.ylabel("The Sum of Interference Score(lower is better)")
plt.xlabel("The Number of Experiment")
plt.gca()
plt.legend()
plt.show()
