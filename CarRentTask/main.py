from Customer import Customer

cust1 = Customer('Rosen')
cust2 = Customer('Diana')

cust1.listcars()
cust1.rent_hour('BH1110AM', 1)
cust1.rent_day('BH0032AK', 1)
cust1.rent_week('BH2532AK', 1)
cust1.finalise()
cust2.listcars()
cust2.rent_hour('BH8763AK', 5)
cust2.finalise()
