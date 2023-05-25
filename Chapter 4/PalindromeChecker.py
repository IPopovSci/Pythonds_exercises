from Deque import Deque

def palindrome_checker(string):
    deque=Deque()
    for ch in string:
        deque.addRear(ch)
    while deque.size()>1:
        palindrome=(deque.removeRear()==deque.removeFront())
        if palindrome==False:
            break
    return palindrome

print(palindrome_checker('racecar'))