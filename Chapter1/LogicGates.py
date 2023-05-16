'''
Create a two new gate classes, one called NorGate the other called NandGate.
NandGates work like AndGates that have a Not attached to the output.
NorGates work lake OrGates that have a Not attached to the output.

Create a series of gates that prove the following equality NOT (( A and B) or (C and D)) is that same as NOT( A and B ) and NOT (C and D).
Make sure to use some of your new gates in the simulation.
'''
'''Q.10 Research other types of gates that exist (such as NAND, NOR, and XOR). 
Add them to the circuit hierarchy. How much additional coding did you need to do?'''
'''Q.11 The most simple arithmetic circuit is known as the half-adder. 
Research the simple half-adder circuit. Implement this circuit.'''


class LogicGate:

    def __init__(self, n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        elif isinstance(self.pinA, Connector):
            return self.pinA.getFrom().getOutput()
        else:  # If the pin is already set to a value
            return self.pinA

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        elif isinstance(self.pinB,Connector):
            return self.pinB.getFrom().getOutput()
        else: #If the pin is already set to a value
            return self.pinB

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")
    def setInput(self):
        return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))

class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


# question 10
class NandGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1


class NorGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 0
        else:
            return 1


class XorGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == b:
            return 0
        else:
            return 1


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0



class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1



class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate
#Q11

class HalfAdder(BinaryGate):
    def __init__(self,n,pinA=None,pinB=None):
        self.sumout = XorGate('Sum')
        self.carry = AndGate('Carry')
        super().__init__(n)
        self.pinA = pinA
        self.pinB = pinB
        if self.pinA== None:
            self.pinA=self.setInput()
        if self.pinB == None:
            self.pinB=self.setInput()



    def getOutput(self):
        self.carry.pinA,self.sumout.pinA = self.pinA,self.pinA
        self.carry.pinB, self.sumout.pinB = self.pinB, self.pinB

        sum_result = self.sumout.getOutput()
        carry_result = self.carry.getOutput()

        return sum_result, carry_result


#Q12 - Now extend that circuit and implement an 8 bit full-adder.
class FullAdder:
    def __init__(self):
        self.ha1 = HalfAdder('ha1')
        self.ha2 = HalfAdder('ha2',None,int())
        self.orgate = OrGate('Orgate')

    def getOutput(self):
        sum_1, c_out1 = self.ha1.getOutput()
        self.ha2.pinB = sum_1

        sum_out, c_out2 = self.ha2.getOutput()

        self.orgate.pinA = c_out2
        self.orgate.pinB = c_out1
        c_out3 =  self.orgate.getOutput()
        return sum_out,c_out3

ha = FullAdder()
print(ha.getOutput())

