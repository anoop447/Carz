class Car(object):
    def __init__(self,distance=2,honk_style='beep beep',color='',line='-'):
        self.distance = distance
        self.honk_style = honk_style
        self.color = color
        self.line = line

    def soundHorn(self):
        print(self.honk_style)

    def getColor(self):
        return self.color

    def showLine(self,distance):
        self.distance += distance
        self.line = self.line + '-' * distance
        return self.line

    def getDistance(self):
        return self.distance


class Model_1(Car):
    def __init__(self,distance=0,honk_style='beep beep',color='',line=''):
        super().__init__(distance,honk_style,color,line)

        self.color = 'blue'

    def getColor(self):
        return super().getColor()

class Model_2(Car):
    def __init__(self,distance=0,honk_style='beep beep',color='',line=''):
        super().__init__(distance,honk_style,color,line)

        self.color = 'red'
        self.honk_style = 'honk honk'

    def getColor(self):
        return super().getColor()



