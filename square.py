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
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0

    max = n**0.5+1
    i = 3

    while i <= max:
        if n % i == 0:
            return 0
        i += 2

    return 1


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
                line.addNumber(number)
            y += 2

        # next = number
        line.printLine(onlyPrimes)


squarePrime(16,True)