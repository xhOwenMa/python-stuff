
from ParkingSystem import ParkingSystem
from Car import Car


def main():
    lot = ParkingSystem(5,5,5)
    car1 = Car(2, 1035)
    lot.addCar(car1.carType)
    exitTime = 1450
    print("Car 1 leaves at {}, it has parking fee: {}".format(exitTime, car1.fee(exitTime)))
    

if __name__ == "__main__":
    main()