from Stack import Stack

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
    print(binary)

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

print(baseConverter(25,2))
print(baseConverter(256,16))