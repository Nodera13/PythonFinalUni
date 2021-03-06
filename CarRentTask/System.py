from Vechicle import Vechicle
import json


class System:
    cost = 0

    file = open('data.json')
    data = json.load(file)
    file.close()
    datadict = {}
    cardict = {}

    for (k, v) in data.items():
        datadict.update({k: v})

    for car in datadict:
        car = Vechicle(datadict[car]['make'], datadict[car]['model'],
                       datadict[car]['fuelconsumption'], datadict[car]['registrationplate'],
                       datadict[car]['hourrate'], datadict[car]['dayrate'],
                       datadict[car]['weekrate'], datadict[car]['status'])
        cardict.update({car.registrationplate: car})

    @staticmethod
    def print_cars():
        print('Check which cars are in stock \n')
        for car in System.cardict.values():
            if car.status == 'avaiable':
                print(car.__str__())

    def rent_car_hour(self, customer, registrationplate, hours):
        for car in self.cardict:
            if registrationplate == car:
                if self.cardict.get(car).status == 'avaiable':
                    self.cardict.get(car).status = 'unavaiable'
                    self.cost = self.cardict.get(car).hourrate * hours
                    customer.rentedcars += 1
                    customer.totalcost += self.cost
                    print(customer.name + ' is renting car: ' + car + ' for ' + str(hours) +
                          ' hours at a cost of ' + str(self.cost) + 'lv a hour')
                else:
                    print('Sorry, ' + customer.name + ', That is not a valid car!')

    def rent_car_day(self, customer, registrationplate, day):
        for car in self.cardict:
            if registrationplate == car:
                if self.cardict.get(car).status == 'avaiable':
                    self.cardict.get(car).status = 'unavaiable'
                    self.cost = self.cardict.get(car).dayrate * day
                    customer.rentedcars += 1
                    customer.totalcost += self.cost
                    print(customer.name + ' is renting car: ' + car + ' for ' + str(day) +
                          ' hours at a cost of ' + str(self.cost) + 'lv a day')
                else:
                    print('Sorry, ' + customer.name + ', That is not a valid car!')

    def rent_car_week(self, customer, registrationplate, week):
        for car in self.cardict:
            if registrationplate == car:
                if self.cardict.get(car).status == 'avaiable':
                    self.cardict.get(car).status = 'unavaiable'
                    self.cost = self.cardict.get(car).weekrate * week
                    customer.rentedcars += 1
                    customer.totalcost += self.cost
                    print(customer.name + ' is renting car: ' + car + ' for ' + str(week) +
                          ' hours at a cost of ' + str(self.cost) + 'lv a week')
                else:
                    print('Sorry, ' + customer.name + ', That is not a valid car!')

    @staticmethod
    def finaliserent(customer):
        print('You are renting: ' + str(customer.rentedcars), end=', ')
        if customer.rentedcars >= 3:
            customer.totalcost = customer.totalcost * 0.7
            print(customer.name + ', you earned a 30% discount. Your total cost has become: ' + str(customer.totalcost) )
            customer.rentedcars = 0
            customer.totalcost = 0
        else:
            print(customer.name + ' your total cost is ' + str(customer.totalcost))
