import random

def generate_random_list(size):
    listnum = [int(random.randrange(1,size)) for n in range(size)]
    return listnum