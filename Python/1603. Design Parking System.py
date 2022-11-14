class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big_spaces = big
        self.medium_spaces = medium
        self.small_spaces = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big_spaces > 0:
                self.big_spaces -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium_spaces > 0:
                self.medium_spaces -= 1
                return True
            else:
                return False
        else:
            if self.small_spaces > 0:
                self.small_spaces -= 1
                return True
            else:
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)