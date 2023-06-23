from timeit import Timer
from Chapter3.Utility import generate_random_list
#My implementation is much slower due to list comprehension
def BubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if all([alist[i+1]>alist[i] for i in range(passnum)]): #Short bubble, stop if already sorted
                break
            elif alist[i]>alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]

# test_list = generate_random_list(10)
# t1 = Timer("bubbleSort(test_list)", "from __main__ import test_list,bubbleSort")
# time_taken = t1.timeit(number=10000)
# print("For my implementation of bubble",time_taken, "milliseconds")

#Implementation from book, fastest
def BookBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

test_list = generate_random_list(100)
t1 = Timer("BookBubbleSort(test_list)", "from __main__ import test_list,BookBubbleSort")
time_taken = t1.timeit(number=100000)
print("For Book implementation of bubble",time_taken, "milliseconds")

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       alist[fillslot],alist[positionOfMax] = alist[positionOfMax],alist[fillslot]

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue