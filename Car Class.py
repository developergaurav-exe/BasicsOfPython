from sys import stdin


class Car:
    
    #Write your constructor and printCarInfo method here.
    def __init__(self, noOfGear = 5, color = 'red'):
        self.noOfGear = noOfGear
        self.color = color

    def printInfo(self):
        print('noOfGear: ',self.noOfGear)
        print('color: ', self.color)



class RaceCar(Car):
    
    #Write your constructor and printRaceCarInfo method here.
    def __init__(self, noOfGear = 5, color = 'red', maxSpeed = 1000):
        self.noOfGear = noOfGear
        self.color = color
        self.maxSpeed = maxSpeed

    def printInfo(self):
        print('noOfGear:',self.noOfGear)
        print('color:', self.color)
        print('maxSpeed:', self.maxSpeed)

        
#Driver's code

noOfGear = int(stdin.readline().rstrip())
color = stdin.readline().rstrip()
maxSpeed = int(stdin.readline().rstrip())
        
raceCar = RaceCar(noOfGear,color,maxSpeed)
raceCar.printInfo()
