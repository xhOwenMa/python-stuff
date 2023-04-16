# obj = Car(carType, enterTime)

# this is me playing around

import math

class Car:

    def __init__(self, carType: int, enterTime: int):
        """
        Constructor

        enterTime : int (time in 24-hr) Ex. a car entered at 10:35 pm would have enterTime 2235
        """

        self.carType = carType
        time = self.convertTime(enterTime)
        self.enterTime = time


    def convertTime(self, time: int) -> float:
        """
        time : int
        return the float number reprenting input time (Ex. 1230 would map to 12.5)
        """

        hour = math.floor(time / 100)
        mins = time - (hour * 100)
        return float(hour + mins / 60)    
    

    def timeCat(self, exitTime: int) -> int:
        """
        exitTime : int, when this car leaves the parking lot
        return what category (int), based on this car's parking time, this car belongs to for charging parking fee
        """

        time = exitTime - self.enterTime
        if time < 2:
            return 1
        elif time > 2 and time < 4:
            return 2
        elif time > 4 and time < 6:
            return 3
        elif time > 6 and time < 10:
            return 4
        else:
            return 5
        
        
    def fee(self, exitTime: int) -> int:
        """
        cat : int, the parking fee category of this car
        return how much this car should be charged
        """
        
        f = [5, 10, 15, 20, 40]
        time = self.convertTime(exitTime)
        cat = self.timeCat(time)
        print(cat)
        
        return f[cat - 1]