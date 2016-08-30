class Fraction:
    def __init__(self, top, bot):
        self.num = top
        self.den = bot
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den
    def __add__(self, otherF):
        newnum = self.num*otherF.getDen() + self.den*otherF.getNum()
        newden = self.den*otherF.getDen()
        self.gcd(newnum, newden)
        return Fraction(self.getNum(), self.getDen())
    def gcd(self, m, n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        self.den = self.den//n
        self.num = self.num//n
