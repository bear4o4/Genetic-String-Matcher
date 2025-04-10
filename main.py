
import random
import string
import matplotlib.pyplot as plt



TARGET = "HELLOGA123"
POPULATION_SIZE = 50
GENOME_LENGTH = 10
MUTATION_RATE = 0.05
CROSSOVER_RATE = 0.8
TOURNAMENT_SIZE = 3
NUM_GENERATIONS = 20

def generate_individual():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=GENOME_LENGTH))
def fitness(individual):
    return sum(1 for i in range(GENOME_LENGTH) if individual[i] == TARGET[i])
def tournament_selection(population):
    tournament = random.sample(population, TOURNAMENT_SIZE)
    tournament.sort(key=lambda x: fitness(x), reverse=True)
    return tournament[0]
def crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return parent1, parent2

    point1 = random.randint(1, GENOME_LENGTH - 1)
    point2 = random.randint(point1, GENOME_LENGTH)

    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2
def mutate(individual):
    return ''.join(
        char if random.random() > MUTATION_RATE else random.choice(string.ascii_uppercase + string.digits)
        for char in individual
    )
def create_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]

def evolve():
    population = create_population()
    max_fitness_per_generation = []
    avg_fitness_per_generation = []

    for generation in range(NUM_GENERATIONS):
        new_population = []
        total_fitness = 0

        while len(new_population) < POPULATION_SIZE:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])
        population = new_population[:POPULATION_SIZE]
        fitness_values = [fitness(ind) for ind in population]
        max_fitness = max(fitness_values)
        avg_fitness = sum(fitness_values) / len(fitness_values)
        max_fitness_per_generation.append(max_fitness)
        avg_fitness_per_generation.append(avg_fitness)
        print(f"Generation {generation + 1} - Max Fitness: {max_fitness} Avg Fitness: {avg_fitness:.2f}")


        if max_fitness == GENOME_LENGTH:
            print("Target string matched!")
            break


    plot_fitness(max_fitness_per_generation, avg_fitness_per_generation)
def plot_fitness(max_fitness, avg_fitness):
    generations = range(1, len(max_fitness) + 1)
    plt.plot(generations, max_fitness, label="Max Fitness")
    plt.plot(generations, avg_fitness, label="Avg Fitness")
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.title("Fitness Progress Over Generations")
    plt.legend()
    plt.show()
evolve()
