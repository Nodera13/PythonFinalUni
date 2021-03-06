from System import System


class Customer:

    def __init__(self, name):
        self.name = name
        self.totalcost = 0.00
        self.rentedcars = 0

    def listcars(self):
        System.print_cars()
        print('Thats all of the cars')

    def rent_hour(self, registrationplate, hours):
        System.rent_car_hour(System , self, registrationplate, hours)

    def rent_day(self, registrationplate, day):
        System.rent_car_day(System , self, registrationplate, day)

    def rent_week(self, registrationplate, week):
        System.rent_car_week(System , self, registrationplate, week)

    def finalise(self):
        System.finaliserent(self)
