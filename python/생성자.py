class FourCal:
    # == 생성자(객체가 생성되는 시점에 자동으로 호출된다.) == 
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        return self.first * self.second
    
    def div(self):
        return self.first // self.second
    
    def sub(self):
        return self.first - self.second

a = FourCal(4, 2)
print(a.first, a.second)
print(a.add(), a.mul())