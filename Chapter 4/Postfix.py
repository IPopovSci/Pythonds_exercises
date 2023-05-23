from Stack import Stack

#This example will only work if we assign proper brackets to infix_expression
def IntoPost(infix_expression):
    opstack = Stack()
    output = []
    operands = ['*','/','+','-']
    infix_expression = list(infix_expression)
    error = False
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

print(IntoPost('((A*B)+(C*D))'))


