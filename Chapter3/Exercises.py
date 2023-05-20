from timeit import Timer
from Utility import generate_random_list
import random

#1.Devise an experiment to verify that the list index operator is O(1)
def list_index_test():
    for i in range(10,50000,5000):
        test_list = list(range(i))
        t1 = Timer("test_list[random.randrange(0, len(test_list))]", "from __main__ import test_list,random")
        time_taken = t1.timeit(number=10000)
        print("list index for size ",i,'is',time_taken, "milliseconds")

#2. Devise an experiment to verify that get item and set item are O(1) for dictionaries.
def dict_gs_test():
    for i in range(10,50000,5000):
        test_dict = {j:None for j in range(i)}
        t_get_item = Timer("test_dict.get(random.randrange(0, len(test_dict)))", "from __main__ import test_dict,random")
        t_set_item = Timer("test_dict[random.randrange(0, len(test_dict))]='test'", "from __main__ import test_dict,random")
        time_taken_get = t_get_item.timeit(number=10000)
        time_taken_set = t_set_item.timeit(number=10000)
        print("get item for dict of size",i,'is',time_taken_get, "milliseconds")
        print("set item for dict of size", i, 'is', time_taken_set, "milliseconds")

#3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.
# I Don't like this implementation, but other implementations I found I liked even less
def del_test():
    for i in range(100,500000,5000):
        test_dict = {j:None for j in range(i)}
        test_list = list(range(i))
        t_list_del = Timer("del test_list[10]", "from __main__ import test_list,random")
        t_dict_del = Timer("del test_dict[10]", "from __main__ import test_dict,random")
        time_taken_get = t_list_del.timeit(number=1)
        print("del item for list of size", i, 'is', time_taken_get * 1000, "milliseconds")
        time_taken_set = t_dict_del.timeit(number=1)
        print("del item for dict of size", i, 'is', time_taken_set*1000, "milliseconds")

#4. Given a list of numbers in random order, write an algorithm that works in O(n*log(n)) to find the kth smallest number in the list.
#This is O(k*n), good enough?
def find_k_smallest(size,k):
    smallest_numbers=[]

    list = generate_random_list(size)
    current_smallest = list[0]
    last_smallest=0
    while len(smallest_numbers)<k:
        for i,number in enumerate(list):
            if number<current_smallest and number>last_smallest:
                current_smallest=number
        last_smallest = current_smallest
        smallest_numbers.append(current_smallest)
        current_smallest = list[0]

    #print(smallest_numbers)

for i in [10,100,1000,10000]:
    size = i
    test = Timer("find_k_smallest(size,10)", "from __main__ import size,find_k_smallest,random")
    time_taken = test.timeit(number=1)
    print("finding k smallest integer in list size", i, 'takes', time_taken*1000, "milliseconds")
