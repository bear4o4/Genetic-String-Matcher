
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
