
import random

## ESTRATEGIES
## 1 COPERATE / 0 NO COPERATE

def TitForTat(iteration: int, own_list: list, other_list: list):

    if iteration==0: return 1

    if other_list[-1]==0 and 0.1>random.random():
        return 1

    return other_list[-1]

def Dumb(iteration: int, own_list: list, other_list: list):

    return 1

def Devil(iteration: int, own_list: list, other_list: list):

    return 0

def Friedman(iteration: int, own_list: list, other_list: list):

    if iteration==0: return 1

    if other_list[-1]==0 or own_list[-1]==0:
        return 0

    return 1

def Joss(iteration: int, own_list: list, other_list: list):

    if iteration==0: return 1

    if 0.1>random.random():
        return 0

    return other_list[-1]
    

def Random(iteration: int, own_list: list, other_list: list):

    if random.random()<0.5:
        return 0

    return 1

def Sample(iteration: int, own_list: list, other_list: list):

    if iteration==0 or iteration==1: return 1

    if other_list[-1]==0 and other_list[-2]==0:
        return 0

    return 1

def Tester(iteration: int, own_list: list, other_list: list):

    if iteration==0: return 0
    
    if iteration==1: return 1

    if iteration>2 and other_list[1]==0:
        return TitForTat(0,own_list,other_list)

    return iteration%2

def Clock(iteration: int, own_list: list, other_list: list):

    if iteration%3==0: return 1

    return 0

## GLOBALS

estrategies = [('Dumb',Dumb), ('TitForTat', TitForTat), ('Friedman',Friedman), ('Random',Random),('Joss',Joss), ('Sample',Sample),('Tester',Tester), ('Devil',Devil),('Clock',Clock)]
#estrategies = [('TitForTat', TitForTat),('Devil',Devil)]


estrategies_score = {'Dumb':0, 'TitForTat':0, 'Devil':0, 'Joss':0,'Random':0, 'Friedman':0, 'Sample':0, 'Tester':0, 'Clock':0}
