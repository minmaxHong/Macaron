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

# == 클래스 상속 == 
class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second
    
# == 오버라이팅(부모 클래스 대신, 오버라이딩한 메서드가 호출된다.) ==
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first // self.second
            
a = SafeFourCal(4, 0)
print(a.div())