class SimpleCar:
    def __init__(self):
        self.miles = 0

    def drive(self, dist):
        self.miles = self.miles + dist
        
    def reverse(self, dist):
        self.miles = self.miles - dist
        
    def get_odometer(self):
        return self.miles
    
    def honk_horn(self):
        print('beep beep')
        
    def report(self):
        print(f'Car has driven: {self.miles} miles')
        
if __name__ == "__main__":
    # TODO: Create SimpleCar object
    simplecar1 = SimpleCar
    simplecar1.miles = 0
    usrinputfwd = int(input())
    usrinputrvrse = int(input())
    # TODO: Drive input number of miles forward
    simplecar1.drive(simplecar1, usrinputfwd)
    # TODO: Drive input number of miles in reverse
    simplecar1.reverse(simplecar1, usrinputrvrse)
    # TODO: Honk the horn
    simplecar1.honk_horn(simplecar1)
    # TODO: Report car status
    simplecar1.report(simplecar1)