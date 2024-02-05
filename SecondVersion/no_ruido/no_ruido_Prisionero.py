
import os
import sys
import random
from Prisioner import Prisioner
from Negotiation_no_ruido import Negotiation
import Estrategies_no_ruido
from Estrategies_no_ruido import estrategies, estrategies_score



def main():

    for int1 in range(len(Estrategies_no_ruido.estrategies)):
    
        for int2 in range(len(Estrategies_no_ruido.estrategies)):

            prio1_args = Estrategies_no_ruido.estrategies[int1]
            prio2_args = Estrategies_no_ruido.estrategies[int2]

            prio1 = Prisioner(prio1_args[0],prio1_args[1])
            prio2 = Prisioner(prio2_args[0],prio2_args[1])
            nego = Negotiation(prio1,prio2, iterations=200)
            nego.start()

    
    print('\n')

    for estr in Estrategies_no_ruido.estrategies_score:
        print(f'Prisioner {estr} - FINAL SCORE: {Estrategies_no_ruido.estrategies_score[estr]}')

    final_list = list(Estrategies_no_ruido.estrategies_score.items())

    final_list.sort(key= lambda x:x[1], reverse=True)

    print('\n')

    print(final_list)


if __name__=='__main__':
    main()
