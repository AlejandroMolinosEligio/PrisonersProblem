
from Prisoner import Prisoner
import random
import Estrategies
from Estrategies import estrategies, estrategies_score

class Negotiation():

    def __init__(self,prio1: Prisoner, prio2: Prisoner, prio1_values: list =[], prio2_values: list =[],prio1_score: int=0, prio2_score:int=0, iterations: int=0):
        self.prio1 = prio1
        self.prio2 = prio2
        self.prio1_values = prio1_values
        self.prio2_values = prio2_values
        self.iterations = iterations
        self.prio1_score = prio1_score
        self.prio2_score = prio2_score

    def start(self, verbose=False):

        for i in range(self.iterations):
            prio1_value = self.prio1.estrategy(i,self.prio1_values,self.prio2_values)
            prio2_value = self.prio2.estrategy(i,self.prio2_values,self.prio1_values)

            if prio1_value==1 and prio2_value==1:
                self.prio1_score += 3
                self.prio2_score += 3
            elif prio1_value == 0 and prio2_value==1:
                self.prio1_score += 5
            elif prio1_value == 1 and prio2_value==0:
                self.prio2_score += 5
            else:
                self.prio1_score += 1
                self.prio2_score += 1
            
            self.prio1_values.append(prio1_value)
            self.prio2_values.append(prio2_value)

        if verbose:

            print(f'Prisoner {self.prio1.name} score: {self.prio1_score}')
            print(f'Prisoner {self.prio2.name} score: {self.prio2_score}')

            print(f'Max score {self.iterations*5} - Min score {str(0)}')

        self.prio1.score+=self.prio1_score
        self.prio2.score+=self.prio2_score
        Estrategies.estrategies_score[self.prio1.name] += self.prio1_score
        Estrategies.estrategies_score[self.prio2.name] += self.prio2_score