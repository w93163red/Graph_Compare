import numpy as np


class GA:
    def __init__(self, matrix):
        self.CROSS_RATE = 0.8
        self.MUTATION_RATE = 0.05
        self.POP_SIZE = 10000
        self.N_TASKS = 10
        self.N_GENERATION = 50
        self.N_CORES = 4
        self.POP = np.random.randint(0, self.N_CORES, size=(self.POP_SIZE, self.N_TASKS))
        self.matrix = matrix

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

    def selection(self):
        fitness = []
        for i in self.POP:
            fitness.append(self.get_fitness(i))
        fitness = np.array(fitness)
        suma = fitness.sum()
        for i in range(len(fitness)):
            fitness[i] = suma - fitness[i]

        pop_ = np.random.choice(np.arange(self.POP_SIZE), self.POP_SIZE, replace=True, p= fitness / fitness.sum())
        return pop_

    def crossover(self, parent1, parent2):
        if np.random.rand() < self.CROSS_RATE:
            parent1 = parent1.tolist()
            parent2 = parent2.tolist()
            child1 = []
            child2 = []
            i = np.random.randint(0, self.N_TASKS)
            child1 = parent1[0:i] + parent2[i:]
            child2 = parent2[0:i] + parent1[i:]
            child1 = np.array(child1)
            child2 = np.array(child2)
            child1 = self.mutate(child1)
            child2 = self.mutate(child2)
            return child1, child2
        return parent1, parent2

    def mutate(self, child):
        for i in range(self.N_TASKS):
            if np.random.rand() < self.MUTATION_RATE:
                child[i] = np.random.randint(0, self.N_CORES, size=1)
        return child

    def evolve(self):
        pop_1 = self.selection()
        pop_2 = self.selection()
        new_pop = []
        for i in range(len(pop_1) // 2):  # for every parent
            child1, child2 = self.crossover(self.POP[pop_1[i]], self.POP[pop_2[i]])
            new_pop.append(child1)
            new_pop.append(child2)
        self.POP = np.array(new_pop)

    def run(self):
        fitness = []
        best_DNA = None
        for generation in range(self.N_GENERATION):
            self.evolve()
            fitness = []
            for i in self.POP:
                fitness.append(self.get_fitness(i))
            best_DNA = self.POP[np.argmin(fitness)]
            #print("Gen", generation, ":", best_DNA, "Score:", self.get_fitness(best_DNA))

        return best_DNA, self.get_fitness(best_DNA)