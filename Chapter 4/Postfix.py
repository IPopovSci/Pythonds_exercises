from Stack import Stack

#This example will only work if we assign proper brackets to infix_expression
def IntoPost(infix_expression):
    opstack = Stack()
    output = []
    operands = ['*','/','+','-']
    infix_expression = list(infix_expression.replace(' ',''))
    switch = False
    for token in infix_expression:
        if token=='(':
            opstack.push(token)
        elif token==')' and not opstack.isEmpty():
            while switch==False:
                if opstack.peek() in operands:
                    output.append(opstack.pop())
                elif opstack.peek() in ['(']:
                    opstack.pop()
                    switch=True
                else:
                    opstack.pop()
            switch=False
        elif token in ['+','-']:
            while (opstack.peek() in operands):
                output+=opstack.pop()
            opstack.push(token)
        elif token in ['*','/']:
            while (opstack.peek() in ['*','/']):
                output+=opstack.pop()
            opstack.push(token)
        elif isinstance(token,str):
            output.append(token)
        else:
            print('Something went horribly wrong')
    return output

def IntoPostImproved(infix_expression):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack = Stack()
    output = []
    operands = ['*','/','+','-']
    infix_expression = list(infix_expression.replace(' ',''))
    for token in infix_expression:
        if token=='(':
            opstack.push(token)
        elif token==')' and not opstack.isEmpty():
            topToken = opstack.pop()
            while topToken != '(':
                output.append(topToken)
                topToken = opstack.pop()
        elif token in operands:
            while (not opstack.isEmpty()) and \
               (prec[opstack.peek()] >= prec[token]):
                  output.append(opstack.pop())
            opstack.push(token)

        elif isinstance(token,str):
            output.append(token)
        else:
            print('Something went horribly wrong')
    while not opstack.isEmpty():
        output.append(opstack.pop())
    return output

#print(print(IntoPostImproved("( A + B ) * C - ( D - E ) * ( F + G )")))

def PostInto(postfix,dir_eval=False):
    opstack = Stack()
    output = []
    operands = ['*','/','+','-']
    postfix = list(postfix.replace(' ',''))
    for token in postfix:

        if token in operands and (not opstack.isEmpty()):
            if token != '/':
                num1=opstack.pop()
                num2=opstack.pop()
                output=('('+num1+token+num2+')')
                opstack.push('('+num1+token+num2+')')
            if token == '/':
                num2 = opstack.pop()
                num1 = opstack.pop()
                output = ('(' + num1 + token + num2 + ')')
                opstack.push('(' + num1 + token + num2 + ')')
        elif token.isdigit() or token.isalpha():
            opstack.push(token)
    if eval==False:
        return output
    else:
        return eval(output)
print(PostInto('7 8 + 3 2 + /',dir_eval=True))

