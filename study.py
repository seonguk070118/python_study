class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
    
class MoreFourCal(FourCal):
    def pow(self):
        result=self.first ** self.second
        return result
a=FourCal(4,2)
b=FourCal(3,8)
c=MoreFourCal(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
print(c.pow())