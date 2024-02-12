
import os
import sys
import random
from Prisioner import Prisioner
from Negotiation import Negotiation
import Estrategies
from Estrategies import estrategies, estrategies_score
import math

population_num = 5*len(Estrategies.estrategies)

populations = []

def generate_initial_population():

    population = []

    general_percent = math.floor(population_num/len(Estrategies.estrategies))

    for item in Estrategies.estrategies:
        population += [Prisioner(item[0],item[1]) for _ in range(general_percent)]
    
    if len(population)<population_num:
        population += [population[-1]] * (population_num-len(population))

    population_estrategy_num = {item[0]: 0 for item in Estrategies.estrategies}

    for prisioner in population:
        population_estrategy_num[prisioner.name]+=1

    return population,population_estrategy_num 

def generate_population(population):

    final_list = list(Estrategies.estrategies_score.items())

    total = sum([x[1] for x in final_list])

    sum_score = sum([x.score for x in population])

    populations.append((population,sum_score))

    if len(populations)>2 and populations[-2][1]>=populations[-1][1]: population = populations[-2]

    num_popula = len(population)

    best = [x for x in population]
    best.sort(key=lambda x:x.score, reverse=True)
    
    new_population = []
    for i in range(num_popula-10):
        item = Estrategies.estrategies[random.randint(0,len(Estrategies.estrategies)-1)]
        new_population.append(Prisioner(item[0],item[1]))

    new_population += best[:10]

    population_estrategy_num = {item[0]: 0 for item in Estrategies.estrategies}

    for prisioner in new_population:
        population_estrategy_num[prisioner.name]+=1

    return new_population,population_estrategy_num,total

def main():

    gen_number = 1000

    population,population_estrategy_num = generate_initial_population()

    print('Initial population:',population_estrategy_num,'\n')

    for gen in range(gen_number+1):

        for int1 in range(len(population)):
    
            for int2 in range(len(population)):

                prio1 = population[int1]
                prio2 = population[int2]
                nego = Negotiation(prio1,prio2, iterations=200)
                nego.start()

        population,population_estrategy_num,total = generate_population(population)

        if gen%50==0:
            final = [(item[0],Estrategies.estrategies_score[item[0]]/total) for item in Estrategies.estrategies]
            final.sort(key= lambda x:x[1], reverse=True)
            print('Gen ',gen,':',final)
            print('Population:',population_estrategy_num,'\n')


if __name__=='__main__':
    main()
