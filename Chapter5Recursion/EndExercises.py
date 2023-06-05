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
            print("Boat can't travel empty")
import sys
sys.setrecursionlimit(10**6)
#This sucks
def travel_problem(bank,boat,people=[0,0,0,1,1,1]):
    done=False
    if len(bank.right)==len(people):
        done=True
        return "Done"
    else:
        #Left side permutations
        #If equal amount of m and c
        #print('bank_left_m',bank.left_m,'bank_right_m:', bank.right_m, 'bank_right_c:', bank.right_c)
        if boat.location==0 and bank.left_m==bank.left_c:
            print('left_m=left_c')
            choice= random.choice(bank.left)
            if choice == 1 and (
                    bank.right_m >= (bank.right_c + 1) or bank.right_m == 0) and bank.left_m >= (bank.left_c + 1):
                boat.load(bank, choice)
            else:
                choice == 0
                boat.load(bank,choice)
            #Roll for another passanger, can be M or C;
            if random.uniform(0, 1)>0.5 and len(bank.left)>0:
                choice = random.choice(bank.left)
                #If cannibal pick, other side should have enough M, or no M at all
                if choice==1 and (bank.right_m>=(bank.right_c+1) or bank.right_m==0):
                    boat.load(bank, choice)
                elif choice==0:
                    boat.load(bank, choice)
            print(f'loaded {choice}, current seating, ', boat.seating)
            boat.transfer(bank)
            print('transferred to right, on left bank', bank.left, 'on right bank', bank.right)
        #If more M than C
        if boat.location==0 and bank.left_m>bank.left_c:
            print('left_m>left_c')
            choice = random.choice(bank.left)
            print('Bank left_m',bank.left_m,'bank left_c',bank.left_c,'bank right m',bank.right_m,'bank right c',bank.right_c)
            if choice == 1 and (
                    bank.right_m >= bank.right_c + 1 or bank.right_m == 0) and bank.left_m >= (bank.left_c + 1):
                boat.load(bank, choice)
                #Need to add double missionary here
            elif (choice == 0 and ((bank.left_m-1)>=bank.left_c)) and ((bank.right_m+2>=bank.right_c) or (bank.right_c==0)):
                    print('wtf choice')
                    print(bank.right_m>=bank.right_c,bank.right_c==0)
                    print('Bank left_m', bank.left_m, 'bank left_c', bank.left_c, 'bank right m', bank.right_m,
                          'bank right c', bank.right_c)
                    boat.load(bank, choice)
                    boat.load(bank, choice)
            else:
                choice=1
                boat.load(bank,choice)
            print('Choice is', choice)
            #Roll for another passanger, can be M or C;
            if random.uniform(0, 1)>0.5 and len(bank.left)>0:
                choice = random.choice(bank.left)
                #If cannibal pick, other side should have enough M, or no M at all AND this side should have enough M
                if choice==1 and (bank.right_m>=bank.right_c+1 or bank.right_m==0) and bank.left_m>=bank.left_c+1:
                    boat.load(bank, choice)
                elif choice==0 and bank.left_m-1>=bank.left_c and not (bank.left_m>=bank.left_c or bank.right_c==0):
                    print(bank.right_m >= bank.right_c or bank.right_c == 0)
                    boat.load(bank, choice)
            print(f'loaded {choice}, current seating, ', boat.seating)
            boat.transfer(bank)
            print('transferred to right, on left bank', bank.left, 'on right bank', bank.right)
        #If not missionairies left on the left
        if boat.location==0 and bank.left_m==0:
            print('left_m=0')
            choice = 1
            boat.load(bank,choice)
            #Roll for another passanger, can be M or C;
            if random.uniform(0, 1)>0.5 and len(bank.left)>0:
                choice = random.choice(bank.left)
                #If cannibal pick, other side should have enough M, or no M at all
                if choice==1 and (bank.right_m>=bank.right_c+1 or bank.right_m==0):
                    boat.load(bank, choice)
            print(f'loaded {choice}, current seating, ', boat.seating)
            boat.transfer(bank)
            print('transferred to right, on left bank', bank.left, 'on right bank', bank.right)

        # Right side permutations
        # If equal amount of m and c
        if boat.location == 1 and bank.right_m == bank.right_c:
            print('Right Side, right_m=right_c')
            print('Bank left_m', bank.left_m, 'bank left_c', bank.left_c, 'bank right m', bank.right_m,
                  'bank right c', bank.right_c)
            if (bank.left_m >= (bank.left_c + 1)) or (bank.left_m == 0):
                print('WTF', (bank.left_m >= (bank.left_c + 1)) )
                choice=1
                boat.load(bank, choice)
            else:
                choice=0
                boat.load(bank, choice)
            print('Bank left_m', bank.left_m, 'bank left_c', bank.left_c, 'bank right m', bank.right_m,
                  'bank right c', bank.right_c)
            # Roll for another passanger, can be M or C;
            if random.uniform(0, 1) > 0.5 and len(bank.right) > 0:
                choice = random.choice(bank.right)
                # If cannibal pick, other side should have enough M, or no M at all
                if choice == 1 and (bank.left_m >= (bank.left_c + 1) or bank.left_m == 0):
                    print('WTF random', (bank.left_m >= (bank.left_c + 1)))
                    boat.load(bank, choice)
                elif choice == 0:
                    boat.load(bank, choice)
            print(f'loaded {choice}, current seating, ', boat.seating)
            boat.transfer(bank)
            print('transferred to left, on left bank', bank.left, 'on right bank', bank.right)
        # If more M than C
        if boat.location ==1 and bank.right_m > bank.right_c:
            print('Right side right m > right c')
            choice = random.choice(bank.right)
            if choice == 1 and (
                    bank.left_m >= bank.left_c + 1 or bank.left_m == 0) and bank.right_m >= bank.right_c + 1:
                boat.load(bank, choice)
            elif choice == 0:
                boat.load(bank, choice)
            # Roll for another passanger, can be M or C;
            if random.uniform(0, 1) > 0.5 and len(bank.right) > 0:
                choice = random.choice(bank.right)
                # If cannibal pick, other side should have enough M, or no M at all AND this side should have enough M
                if choice == 1 and (
                        bank.left_m >= (bank.left_c + 1) or bank.left_m == 0) and bank.right_m >= (bank.right_c + 1):
                    boat.load(bank, choice)
                elif choice == 0 and (bank.left_m >= (bank.left_c + 1) or bank.left_m == 0) and bank.right_m >= (bank.right_c + 1) :
                    boat.load(bank, choice)
            print(f'loaded {choice}, current seating, ', boat.seating)
            boat.transfer(bank)
            print('transferred to left, on left bank', bank.left, 'on right bank', bank.right)
        # If not missionairies left on the right
        if boat.location == 1 and bank.right_m == 0:
            print('right side right m == 0')
            choice = 1
            boat.load(bank, choice)
            #Roll for another passanger, can be M or C;
            # if random.uniform(0, 1) > 0.5 and len(bank.right) > 0:
            #     choice = 1
            #     # If cannibal pick, other side should have enough M, or no M at all
            #     if choice == 1 and (bank.left_m >= bank.left_c + 1 or bank.left_m == 0):
            #         boat.load(bank, choice)
            print(f'loaded {choice}, current seating, ', boat.seating)
            boat.transfer(bank)
            print('transferred to left, on left bank', bank.left, 'on right bank', bank.right)

    travel_problem(bank,boat)

bank_problem=bank([0,0,0,1,1,1])
boat_problem=boat(2)
travel_problem(bank_problem,boat_problem)

# while True:
#     print('Boat location ', boat.location)
#     while boat.location==0:
#         if bank.left_m>=bank.left_c and len(boat.seating)<boat.num_seats and bank.left_c>1:
#             boat.load(bank,1)
#             print('loaded cannibal, current seating, ', boat.seating)
#         else:
#             boat.load(bank,0)
#             print('loaded missionary, current seating, ', boat.seating)
#         if len(boat.seating) == 2:
#             boat.transfer(bank)
#             print('transferred, on left bank', bank.left, 'on right bank', bank.right)
#
#     while boat.location==1:
#             boat.load(bank,1)
#             print('loaded cannibal, current seating, ', boat.seating)
#             boat.transfer(bank)
#             print('transferred, on left bank', bank.left, 'on right bank', bank.right)
