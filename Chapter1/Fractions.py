'''To make sure you understand how operators are implemented in Python classes, and how to properly write methods,
write some methods to implement *, /, and - . Also implement comparison operators > and <'''
'''1. Implement the simple methods getNum and getDen that will return the numerator and denominator of a fraction.'''
'''2. In many ways it would be better if all fractions were maintained in lowest terms right from the start. 
Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately. 
Notice that this means the __add__ function no longer needs to reduce. Make the necessary modifications.'''
'''3. Implement the remaining simple arithmetic operators (__sub__, __mul__, and __truediv__).'''
'''4. Implement the remaining relational operators (__gt__, __ge__, __lt__, __le__, and __ne__)'''
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         self.common = gcd(top, bottom)
         self.num = top//self.common
         self.den = bottom//self.common


     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def getNum(self):
         return self.num
     def getDen(self):
         return self.den

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         return Fraction(newnum,newden)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum
     def __mul__(self, other):
         newnum = self.num*other.num
         newden = self.den*other.den
         return Fraction(newnum,newden)
     def __truediv__(self, other):
         newnum = self.num*other.den
         newden = self.den * other.num
         return Fraction(newnum, newden)
     def __sub__(self, other):
         newnum = (self.num*other.den - self.den*other.num)
         newden = self.den*other.den
         return Fraction(newnum, newden)
     def __lt__(self, other):
         a_newnum = self.num*other.den
         b_newnum = other.num*self.den
         return a_newnum<b_newnum
     def __gt__(self, other):
         a_newnum = self.num*other.den
         b_newnum = other.num*self.den
         return a_newnum>b_newnum
     def __ge__(self, other):
         a_newnum = self.num*other.den
         b_newnum = other.num*self.den
         return a_newnum>=b_newnum
     def __le__(self, other):
         a_newnum = self.num * other.den
         b_newnum = other.num * self.den
         return a_newnum <= b_newnum
     def __ne__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum != secondnum
x = Fraction(1,3)
y = Fraction(2,3)
print(x+y) #7/6
print(x == y) #False
print(x*y) #1/3
print(x/y) #3/4
print(x-y) #(-1/6)
print(x<y) #True
print(x>y) #False