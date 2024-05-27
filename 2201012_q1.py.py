import random
import math
def f(x):
    return x**2 - 4*x + 4
def Hill_Climbing(Initial_x, Step_size, Max_Iterations):
    current_x = Initial_x
    for k in range(Max_Iterations):
        next_x = current_x + random.uniform(-Step_size, Step_size)
        if f(next_x) < f(current_x):
            current_x = next_x
    return current_x
def Binary_representation(x):

    Binary_string = bin(int((x + 10) * 100))[2:]
    return '0' * (14 - len(Binary_string)) + Binary_string

def Crossover(Parent1, Parent2):
    crossover_point = random.randint(0, len(Parent1))
    Child1 = Parent1[:crossover_point] + Parent2[crossover_point:]
    Child2 = Parent2[:crossover_point] + Parent1[crossover_point:]
    return Child1, Child2

def mutation(Individual, mutation_rate):
    mutated_individual = ''
    for bit in Individual:
        if random.random() < mutation_rate:
            mutated_individual += '1' if bit == '0' else '0'
        else:
            mutated_individual += bit
    return mutated_individual

def Genetic_Algorithm(population_size, mutation_rate, Max_generations):
    population = [Binary_representation(random.uniform(-10, 10)) for _ in range(population_size)]
    for generation in range(Max_generations):
        fitness_scores = [f(int(individual, 2)) for individual in population]
        parents = random.choices(population, weights=fitness_scores, k=2)
        child1, child2 = Crossover(parents[0], parents[1])
        child1 = mutation(child1, mutation_rate)
        child2 = mutation(child2, mutation_rate)
        population[fitness_scores.index(max(fitness_scores))] = child1
        population[fitness_scores.index(min(fitness_scores))] = child2
    return int(population[fitness_scores.index(min(fitness_scores))], 2)

initial_x = random.uniform(-10, 10)
step_size = 0.1
max_iterations = 1000

population_size = 20
mutation_rate = 0.1
max_generations = 100

hill_climbing_solution = Hill_Climbing(initial_x, step_size, max_iterations)

genetic_algorithm_solution = Genetic_Algorithm(population_size, mutation_rate, max_generations)

print("Hill_Climbing solution:", hill_climbing_solution)
print("genetic algorithm solution:", genetic_algorithm_solution)
print("function Value at hill climbing Solution:", f(hill_climbing_solution))
print("function Value at genetic algorithm Solution:", f(genetic_algorithm_solution))
