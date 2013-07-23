__author__ = 'remoliebi'
from math import *


class Line:
    line = ""
    numberLine=""
    digit = 0

    def addNumber(self, number):
        if self.digit == 0:
            self.digit = int(log10(number))+1
        if isprime(number):
            self.line += "O"
        else:
            self.line += " "

        self.numberLine += (" " + str(number).zfill(self.digit))
    def printLine(self,onlyPrimes):
        if onlyPrimes:
            print(self.line)
            self.line = ""
        else:
            print(self.numberLine)
            self.numberLine = ""


def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def squarePrime(x,onlyPrimes):
    if x & 1:
        return False
    y = x
    line = Line()
    for l in range(x):
        specialCount = (x-y)/2
        if l < (x/2):
            for s in range(int(specialCount)):
                number = int(pow(x-2-2*s, 2)+l-s)
                line.addNumber(number)

            for s in range(y):
                number = int(pow(y, 2)-s)
                line.addNumber(number)
            for s in reversed(range(int(specialCount))):
                number = int(pow(x - 2*s, 2) - (x - 2*s) - (specialCount-1 - s))
                # print(x,l,s,number, specialCount)
                line.addNumber(number)
            y -= 2

        if l >= (x/2):

            for s in range(int(specialCount)):
                number = int(pow(x-2-2*s, 2)+l-s)
                last = number+1
                line.addNumber(number)

            for s in range(y):
                number = last
                last += 1
                line.addNumber(number)
            for s in reversed(range(int(specialCount))):
                number = int(pow(x - 2*s, 2) - (2 * l) - (s - 1 + specialCount) + (s * 4))
                # print(x,l,s,specialCount,pow(x-2*s,2), number)

                line.addNumber(number)
            y += 2

        # next = number
        line.printLine(onlyPrimes)


squarePrime(16,False)