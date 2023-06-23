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

#Shell sort - sublists -> insertion sort
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)

        mergeSort(righthalf)

        i=0
        j=0
        k=0
        print('lefthalf=',lefthalf,'righthalf=',righthalf)
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
            print('first while','i=',i,'j=',j,'k=',k)
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
            print('second while', 'i=', i, 'j=', j,'k=',k)
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            print('third while', 'i=', i, 'j=', j,'k=',k)
    print("Merging ",alist)

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first] #Better choose median of 3 as pivot value


   leftmark = first+1
   rightmark = last
   pivotvalue = sorted([alist[first], alist[(first+last)//2], alist[last]])[1] #Median of 3 method - sort is nlogn so it's fine

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark] #Swap if values on the wrong side of the pivot

   alist[first],alist[rightmark] = alist[rightmark],alist[first] #Swap rightmark and the pivot


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
