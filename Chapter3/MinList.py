import random
from Chapter3.TimerDecor import timer
import timeit
from Utility import generate_random_list
@timer
def min_num_n2(listnum):
    smallest_number = listnum[0]
    for number in listnum:
        for i,compare in enumerate(listnum):
            if number < listnum[i] and number<smallest_number:
                smallest_number=number
    print('Smallest number is ', smallest_number)

@timer
def min_num_n(listnum):
    smallest_number = listnum[0]
    for i,_ in enumerate(listnum):
        if listnum[i]<smallest_number:
            smallest_number=listnum[i]
    print('Smallest number is ', smallest_number)

for i in [1000,10000,100000,1000000]:
    listnum = generate_random_list(i)
    print(min(listnum))
    min_num_n2(listnum)