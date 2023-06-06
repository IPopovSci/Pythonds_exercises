import random
#1. Write a recursive function to compute the factorial of a number.

def rec_factorial(num):
    if num<=0: #base case
        return 1
    else:
        factorial=num*rec_factorial(num-1) #recursion
    return factorial

#2. Write a recursive function to reverse a list.

def reverse_list(input_list):
    if len(input_list)==0:
        return []
    else:
        return [input_list[-1]] + reverse_list(input_list[:-1])


#5. Write a recursive function to compute the Fibonacci sequence. How does the performance of the recursive function compare to that of an iterative version?

def fib(a,b,cutoff):
    if b>=cutoff:
        return 'Done'
    else:
        print(a)
        term=a+b
        a=b
        b=term
        return fib(a,b,cutoff)
#print(fib(0,1,1000))

'''Write a program to solve the following problem: You have two jugs: a 4-gallon jug and a 3-gallon jug. \ 
Neither of the jugs have markings on them. There is a pump that can be used to fill the jugs with water. \
 How can you get exactly two gallons of water in the 4-gallon jug?'''
class jug:
    def __init__(self,volume):
        self.volume=volume
        self.water=0

    def fill(self):
        self.water=self.volume
    def empty(self):
        self.water=0

    def transfer(self,jug):
        if jug.water+self.water<=jug.volume:
            jug.water+=self.water
            filled=self.water
        elif jug.water+self.water>jug.volume:
            filled = jug.volume-jug.water
            jug.water=jug.volume

        self.water-=filled

def jug_solver(jug1,jug2,target):
    done=False
    if (jug1.water==target) or (jug2.water==target):
        done=True
        print('Final state: ', jug1.water, jug2.water)
    elif not done:
        if jug1.water==0:
            jug1.fill()
            print('Fill jug1, water levels, ',jug1.water,jug2.water)
        if jug1.water!=0:
            jug1.transfer(jug2)
            print('Transfer from jug1 to jug2, water levels, ', jug1.water, jug2.water)
        if jug2.water==jug2.volume:
            jug2.empty()
            print('Empty jug2, water levels, ', jug1.water, jug2.water)
        jug_solver(jug1, jug2,target)



'''11.Write a program that solves the following problem: Three missionaries and three cannibals come to a river and find a boat that holds two people. \ 
Everyone must get across the river to continue on the journey. However, if the cannibals ever outnumber the missionaries on either bank, \ 
the missionaries will be eaten. Find a series of crossings that will get everyone safely to the other side of the river.'''
#Boat must have at least 1 person
#This is probably violation of geneva convention, but it works, badly.
class bank:
    def __init__(self,people): #0 for missionaries, 1 for cannibals,-1 for empty; people ->list
        self.left = people
        self.right= []
        self.left_m = people.count(0)
        self.left_c = people.count(1)
        self.right_m = int()
        self.right_c = int()

class boat:
    def __init__(self,seats):
        self.num_seats=seats
        self.seating=[]
        self.location=0 #0 for left, 1 for right
    def load(self,bank,to_transfer):
        if self.location==0:
            idx=bank.left.index(to_transfer)
            self.seating.append(bank.left.pop(idx))
            bank.left_m = bank.left.count(0)
            bank.left_c = bank.left.count(1)
        else:
            idx=bank.right.index(to_transfer)
            self.seating.append(bank.right.pop(idx))
            bank.right_m = bank.right.count(0)
            bank.right_c = bank.right.count(1)


    def transfer(self,bank): #to_transfer->list
        if len(self.seating)!=0:
            if self.location==0:
                self.location=1
                bank.right.extend(self.seating)
                self.seating=[]
                bank.right_m = bank.right.count(0)
                bank.right_c = bank.right.count(1)
            else:
                self.location=0
                bank.left.extend(self.seating)
                self.seating=[]
                bank.left_m=bank.left.count(0)
                bank.left_c=bank.left.count(1)
        else:
            raise Exception('Boat can"t travel empty')
cache=[{(0,0,0,1,1,1):()}]
moves = [[0, 0], [1, 1], [0, 1], [1], [0]]
def move_choice(moves,boat,bank,step):


    if step % 2 == 0:
        boat.location = 0
    else:
        boat.location = 1
    while len(boat.seating)==0:
        load_choice = random.choice(moves)
        for choice in load_choice:
            if boat.location == 0 and choice in bank.left:

                boat.load(bank, choice)
                print('Choice', choice, 'bank left', bank.left, boat.seating)
            elif boat.location == 1 and choice in bank.right:
                # print('Choice is',choice)

                boat.load(bank, choice)
                print('Choice', choice, 'bank right', bank.right, boat.seating)
            else:
                return move_choice(moves,boat,bank,step)
    else:
        return boat,bank
def recursive_boat(bank,boat,cache,step,moves):
    fail=False

    if step % 2 == 0:
        boat.location = 0
    else:
        boat.location = 1
    print('-'*10,len(bank.right))
    while not fail:
        print('step #',step,step % 2)

        #print(moves)
        #load_choice=random.choice(moves)
        #print('load choice',load_choice)
        print('from', boat.location)
        boat,bank=move_choice(moves,boat,bank,step)
        boat.transfer(bank)
        #print('Transferred ', boat.seating, 'to', boat.location)

        print('On left side: ', bank.left, 'on right side:', bank.right)

        if (bank.left_c>bank.left_m and (not bank.left_m==0)) or (bank.right_c>bank.right_m and (not bank.right_m==0)):
            print('fail')
            if step>=1:
                step-=1
                cache=cache[:-1]
            else:
                step=0
                cache=[{(0,0,0,1,1,1):()}]
            bank.left = list(list(cache[step].keys())[0])
            bank.right = list(list(cache[step].values())[0])
            print('cache',cache)
            #moves = [move for move in moves if move != load_choice]

            if len(moves)==0:
                moves = [[0, 0], [1, 1], [0, 1], [1], [0]]

            if step % 2 == 0:
                boat.location = 0
            else:
                boat.location = 1
            #fail=True #why the heck did this broke everything
            #return recursive_boat(bank,boat,cache,step,moves)
        else:
            print('success')
            moves = [[0, 0], [1, 1], [0, 1], [1], [0]]
            step += 1

            print('boat location',boat.location)
            cache.append({tuple(bank.left):tuple(bank.right)})
            if len(bank.right) == 6:
                fail = True
                return print(cache)
    if not fail:
        return recursive_boat(bank, boat, cache, step, moves)
    else:
        fail=True
        return 'Done'
# input_bank=bank([0,0,0,1,1,1])
# input_boat=boat(2)
# recursive_boat(input_bank,input_boat,cache,0,moves)
#Pascal Triangle
def pascal_triangle(n):
    if n==1:
        print('[1]'.center(100, ' '))
        print('[1,1]'.center(100, ' '))
        return [1,1]
    else:
        old_row = pascal_triangle(n-1)
        new_row=[1]
        for i in range(len(old_row)-1):
            new_row.append(old_row[i]+old_row[i+1])
        new_row.append(1)
        print(f'{new_row}'.center(100, ' '))
        return new_row


pascal_triangle(n=10)
