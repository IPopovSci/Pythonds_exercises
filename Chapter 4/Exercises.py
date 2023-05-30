from Stack import Stack
import copy
#Write a function revstring(mystr) that uses a stack to reverse the characters in a string.
def revstring(mystr):
    revstr = str()
    stack = Stack()
    for char in mystr:
        stack.push(char)
    while not stack.isEmpty():
        revstr += stack.pop()
    return revstr

#print(revstring("Oh, Look at me, I'm a fancy string!"))

def parchecker(mystr):
    stack = Stack()
    error = False
    for char in mystr:
        if char == '(':
            stack.push(char)
        elif char == ')' and not stack.isEmpty():
            stack.pop()
        elif char == ')' and stack.isEmpty():
            error = True
            break
    if stack.isEmpty() and not error:
        print('Brackets are properly balanced')
    else:
        print('Brackets are not properly balanced')

#parchecker('((myfunc),something)')
#parchecker('((myfunc),something))')
#parchecker('(())))myfunc),something))')

def genparchecker(mystr):
    stack = Stack()
    error = False
    brackets = ['(','{','[']
    close_brackets = [')','}',']']
    for char in mystr:
        if char in brackets:
            stack.push(char)
        elif char in close_brackets and not stack.isEmpty():
            pop_char = stack.pop()
            if brackets.index(pop_char) != close_brackets.index(char):
                error = True
        elif char in brackets and stack.isEmpty():
            error = True
            break
    if stack.isEmpty() and not error:
        print('Brackets are properly balanced')
    else:
        print('Brackets are not properly balanced')

# genparchecker('{ { ( [ ] [ ] ) } ( ) }')
#
# genparchecker('[ [ { { ( ( ) ) } } ] ]')
#
# genparchecker('[ ] [ ] [ ] ( ) { }')
#
# genparchecker('( [ ) ]')
#
# genparchecker('( ( ( ) ] ) )')
#
# genparchecker('[ { ( ) ]')

def divideBy2(integer):
    stack = Stack()
    binary = str()
    while integer:
        remainder = integer % 2
        integer = integer//2
        stack.push(remainder)
    while not stack.isEmpty():
        binary += str(stack.pop())
    return stack,binary

#divideBy2(233)

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"
    stack = Stack()
    newbasenum = str()
    while decNumber:
        remainder = decNumber % base
        decNumber = decNumber//base
        stack.push(remainder)
    while not stack.isEmpty():
        newbasenum += digits[stack.pop()]
    return newbasenum

# print(baseConverter(25,2))
# print(baseConverter(256,16))

#1.Convert the following values to binary using “divide by 2.” Show the stack of remainders.
'''
    17
    45
    96
'''
def divideBy2(integer):
    stack = Stack()
    binary = str()
    while integer:
        remainder = integer % 2
        integer = integer//2
        stack.push(remainder)
    stack_copy=copy.deepcopy(stack)
    while not stack.isEmpty():
        binary += str(stack.pop())
    return binary,list(stack_copy)
print('Exercise 1:Convert the following values to binary using “divide by 2.” Show the stack of remainders')
print(divideBy2(17))
print(divideBy2(45))
print(divideBy2(96))

'''2.Convert the following infix expressions to prefix (use full parentheses):
    (A+B)*(C+D)*(E+F)
    A+((B+C)*(D+E))
    A*B*C*D+E+F
Answer:
1. **+AB+CD+EF
2. +A*+BC+DE
3. ++***ABCDEF
'''
'''3. Convert the above infix expressions to postfix (use full parentheses).
Answer:
1. AB+CD+*EF+*
2. ABC+DE+*+
3. AB*C*D*E+F+'''

'''4. Convert the above infix expressions to postfix using the direct conversion algorithm. Show the stack as the conversion takes place.'''
from Postfix import IntoPostImproved
IntoPostImproved('( A + B ) * ( C + D ) * ( E + F ) ')

