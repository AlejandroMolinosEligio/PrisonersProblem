
import os
import sys
import random
from Prisioner import Prisioner
from Negotiation import Negotiation
import Estrategies
from Estrategies import estrategies, estrategies_score
import math
import copy

population_num = 6*len(Estrategies.estrategies)

populations = []

def uniform_cross(population,size):

    fathers = list(set(x.name for x in population))
    estrs = [x[0] for x in Estrategies.estrategies]

    for _ in range(size):
        if 0.1>random.random():
            item = Estrategies.estrategies[random.randint(0,len(Estrategies.estrategies)-1)]
            population.append(Prisioner(item[0],item[1]))

        else:
            estr = fathers[random.randint(0,len(fathers)-1)]
            item = Estrategies.estrategies[estrs.index(estr)]
            population.append(Prisioner(item[0],item[1]))
    
    return population


def pairs(population):

    population_aux = copy.deepcopy(population)
    new_population = []
        
    while len(population_aux)!=0:

        pair = random.sample(population_aux,k=2)
        if pair[0].score>=pair[1].score:
            new_population.append(pair[0])
        else:
            new_population.append(pair[1])
        
        population_aux = [x for x in population_aux if x not in pair]
            
    new_population = uniform_cross(new_population, len(population)-len(new_population))

    return new_population

def generate_initial_population():

    global population_num

    population = []
    print('Número total de pobalción:', population_num)
    first = int(input(f'¿Cuantos individuos de {Estrategies.estrategies[0][0]}?: '))

    general_percent = math.floor(population_num/len(Estrategies.estrategies))

    for _ in range(first):
        population.append(Prisioner(Estrategies.estrategies[0][0],Estrategies.estrategies[0][1]))

    for _ in range(population_num-first):
        population.append(Prisioner(Estrategies.estrategies[1][0],Estrategies.estrategies[1][1]))

    population_estrategy_num = {item[0]: 0 for item in Estrategies.estrategies}

    for prisioner in population:
        population_estrategy_num[prisioner.name]+=1

    return population,population_estrategy_num 

def generate_population(population):

    final_list = list(Estrategies.estrategies_score.items())

    total = sum([x[1] for x in final_list])

    sum_score = sum([x.score for x in population])

    populations.append((population,sum_score))

    if len(populations)>2 and populations[-2][1]>=populations[-1][1]: 
        populations.pop()
        population = populations[-1][0]

    new_population = pairs(population)

    population_estrategy_num = {item[0]: 0 for item in Estrategies.estrategies}

    for prisioner in new_population:
        population_estrategy_num[prisioner.name]+=1

    return new_population,population_estrategy_num,total

def main():

    gen_number = 1000
    
#    population = [Estrategies.estrategies[0]] * 4 + [Estrategies.estrategies[1]] * 6 + [Estrategies.estrategies[2]] * 5

#    population_estrategy_num = [('TitForTat',4),('Devil',6),('Joss',5)]

    population,population_estrategy_num = generate_initial_population()

    print('[!] Initial population:',population_estrategy_num,'\n')

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
            print('[!] Gen ',gen,':',final)
            print('[!] Population:',population_estrategy_num,'\n')
        else:
            print('[*] Gen',gen,end='\r')

if __name__=='__main__':
    main()


'''

EL ERROR ES QUE SE PUEDE MEJORAR LA FUNCIÓN DE ESOCGER EL MEJOR

'''
