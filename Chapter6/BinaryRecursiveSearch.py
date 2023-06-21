def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return pos
#Due to python slicing being O(k), this isn't strictly log(n) time.
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint + 1:], item)
    return found
#This avoids slicing, making it log(n) time
def binarySearch_logtime(alist,item,first,last):
    found=False
    if len(alist) == 0:
        return False
    else:
        if first<=last:
            midpoint = (first+last)//2
            if alist[midpoint] == item:
                return True
            else:
                if item < alist[midpoint]:
                    last=midpoint-1
                    return binarySearch_logtime(alist,item,first,last)
                else:
                    first=midpoint+1
                    return binarySearch_logtime(alist,item,first,last)
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch_logtime(testlist, 3,0,len(testlist)-1))
print(binarySearch_logtime(testlist, 13,0,len(testlist)-1))