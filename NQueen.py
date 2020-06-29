import random
maxFitness = 28

class NQueen:
    def generate_population(self): #making random chromosomes
        population = []
        for _ in range(100):
            population.append([ random.randint(0, self.no_of_queens) for _ in range(self.no_of_queens)])
        return population


    def fitness(self, chromosome):
        horizontal_collisions = sum([chromosome.count(queen) - 1 for queen in chromosome]) / 2
        row_col_clashes = abs(len(chromosome) - len(set(chromosome)))

        n = len(chromosome)
        left_diagonal = [0] * 2 * n
        right_diagonal = [0] * 2 * n
        for i in range(n):
            left_diagonal[i + chromosome[i] - 1] += 1
            right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

        diagonal_collisions = 0
        for i in range(2 * n - 1):
            counter = 0
            if left_diagonal[i] > 1:
                counter += left_diagonal[i] - 1
            if right_diagonal[i] > 1:
                counter += right_diagonal[i] - 1
            diagonal_collisions += counter / (n - abs(i - n + 1))

        return int(maxFitness - (horizontal_collisions + diagonal_collisions))

    def probability(self,individual, fitness):
        return fitness(individual) / maxFitness

    def random_pick(self,population, probabilities):
        populationWithProbabilty = zip(population, probabilities)
        total = sum(w for c, w in populationWithProbabilty)
        r = random.uniform(0, total)
        upto = 0
        for c, w in zip(population, probabilities):
            if upto + w >= r:
                return c
            upto += w
        assert False, "Shouldn't get here"

    def reproduce(self,x, y):
        n = len(x)
        c = random.randint(0, n - 1)
        return x[0:c] + y[c:n]

    def mutate(self,x):
        n = len(x)
        c = random.randint(0, n - 1)
        m = random.randint(1, n)
        x[c] = m
        return x

    def genetic_queen(self,population, fitness):
        mutation_probability = 0.03
        new_population = []
        probabilities = [self.probability(n, fitness) for n in population]
        for i in range(len(population)):
            x = self.random_pick(population, probabilities)
            y = self.random_pick(population, probabilities)
            child = self.reproduce(x, y)
            if random.random() < mutation_probability:
                child = self.mutate(child)
            #print("{},  fitness = {}".format(str(x), nq.fitness(x)))
            new_population.append(child)
            if fitness(child) == 28: break
        return new_population

    def find(self, no_of_queens):
        self.no_of_queens = no_of_queens
        population = self.generate_population()
        #population_fitness = [self.fitness(x) for x in population]
        generation = 1

        while not 28 in [self.fitness(x) for x in population]:
            #print("=== Generation {} ===".format(generation))
            population = self.genetic_queen(population, self.fitness)
            #print("Maximum fitness = {}".format(max([self.fitness(n) for n in population])))
            generation += 1

        #print("Solved in Generation {}!".format(generation - 1))
        for x in population:
            if self.fitness(x) == 28:
                print("{},  fitness = {}".format(str(x), self.fitness(x)))
                return x


if __name__ == "__main__":
    nq=NQueen()
    no_of_queens = 8
    #int(input("Enter Number of Queens: "))
    maxFitness = int((no_of_queens * (no_of_queens - 1)) / 2)
    seq =nq.find(no_of_queens)
    print(nq.fitness(seq))



