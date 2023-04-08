# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# LeetCode 1603. Design Parking System

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        """
        Constructor: initiate two arrays, one to store the limit and one to store the count
        """

        # this is not to modifies, this keeps account of how many lots there are for each type of car
        self.limit = [big, medium, small]

        # starts at 0 because there are no cars in the beginning
        self.count = [0, 0, 0]
        

    def addCar(self, carType: int) -> bool:
        """
        carType : int, what type of car (1 - big; 2 - medium; 3 - small)
        return True if there are available space; False otherwise
        """

        index = carType - 1
        if self.count[index] < self.limit[index]:
            self.count[index] += 1
            return True

        return False
        