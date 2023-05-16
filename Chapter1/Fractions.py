'''To make sure you understand how operators are implemented in Python classes, and how to properly write methods,
write some methods to implement *, /, and - . Also implement comparison operators > and <'''
'''1. Implement the simple methods getNum and getDen that will return the numerator and denominator of a fraction.'''
'''2. In many ways it would be better if all fractions were maintained in lowest terms right from the start. 
Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately. 
Notice that this means the __add__ function no longer needs to reduce. Make the necessary modifications.'''
'''3. Implement the remaining simple arithmetic operators (__sub__, __mul__, and __truediv__).'''
'''4. Implement the remaining relational operators (__gt__, __ge__, __lt__, __le__, and __ne__)'''
'''5. Modify the constructor for the fraction class so that it checks to make sure that the numerator and denominator are both integers. 
If either is not an integer the constructor should raise an exception.'''
'''6. In the definition of fractions we assumed that negative fractions have a negative numerator and a positive denominator. 
Using a negative denominator would cause some of the relational operators to give incorrect results. 
In general, this is an unnecessary constraint. 
Modify the constructor to allow the user to pass a negative denominator so that all of the operators continue to work properly.'''
'''7. Research the __radd__ method. How does it differ from __add__? When is it used? Implement __radd__.'''
'''8. Repeat the last question but this time consider the __iadd__ method.'''
'''9. Research the __repr__ method. How does it differ from __str__? When is it used? Implement __repr__.'''

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         #Question 5
         if not (isinstance(top, int) or isinstance(bottom, int)):
             raise RuntimeError('Numerator and denominator must be integers!')
         #Question 6
         if bottom<0:
             top*=-1
             bottom=abs(bottom)
         #Question 2
         self.common = gcd(top, bottom)
         self.num = top//self.common
         self.den = bottom//self.common


     def __str__(self):
         return f'{self.num}/{self.den}'
     #Question 9
     def __repr__(self):
         return f"Fraction({self.numerator}, {self.denominator})"

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
     #Question 7
     def __radd__(self,other):
         return other.__add__(self)
     #Question 8
     def __iadd__(self, other):
         return self.__add__(other)
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
x = Fraction(1,2)
y = Fraction(2,3)
print(x+y) #7/6
print(x == y) #False
print(x*y) #1/3
print(x/y) #3/4
print(x-y) #(-1/6)
print(x<y) #True
print(x>y) #False
