import numpy as np
import matplotlib.pyplot as plt

brute_file = open("time/brute_time.txt", "r")
ga_file = open("time/ga_time.txt", "r")
greedy_file = open("time/greedy_time.txt", "r")
mga_file = open("time/mga_time.txt", "r")
gp_file = open("time/graph_time.txt", "r")

brute = []
ga = []
greedy = []
mga = []
gp = []

for i in range(100):
    f = brute_file.readline()
    brute.append(float(f))
    f = ga_file.readline()
    ga.append(float(f))
    f = greedy_file.readline()
    greedy.append(float(f))
    f = mga_file.readline()
    mga.append(float(f))
    f = gp_file.readline()
    gp.append(float(f))

x = [i for i in range(100)]
#plt.plot(x,brute, label="Brute Force Algorithm", marker='*')
# plt.plot(x, ga, label="Genetic Algorithm", marker='*')
# plt.plot(x, mga, label="Microbial Genetic Algorithm", marker='*')
# plt.plot(x, greedy, label="Greedy Algorithm", marker='*')
# plt.plot(x, gp, label="Graph Parition Algorithm", marker='*')
# plt.ylabel("Running time in seconds(lower is better)")
# plt.xlabel("The Number of Experiment")
# plt.gca()
# plt.legend()
# plt.show()

print("ga = %f, mga = %f, greedy = %f, gp = %f, brute force = %f" % (sum(ga) / len(ga), sum(mga) / len(mga),
                                                                     sum(greedy) / len(greedy), sum(gp) / len(gp),
                                                                     sum(brute) / len(brute)) )
