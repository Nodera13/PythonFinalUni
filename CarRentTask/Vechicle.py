class Vechicle(object):
    def __init__(self, make, model, fuelconsumption, registrationplate, hourrate, dayrate, weekrate, status):
        self.make = make
        self.model = model
        self.fuelconsumption = fuelconsumption
        self.registrationplate = registrationplate
        self.hourrate = hourrate
        self.dayrate = dayrate
        self.weekrate = weekrate
        self.status = status

    def __str__(self):
        return f'{self.make} {self.model} {self.registrationplate} with consumption {self.fuelconsumption} \n' \
               f'and rates Hour:{self.hourrate} Day:{self.dayrate} Week:{self.weekrate} \n'
