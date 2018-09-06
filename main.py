#!/usr/bin/python
import MySQLdb

abccars = MySQLdb.connect(host="localhost",
			user="abccars",
			passwd="abccars",
			db="abcCars")

cur = abccars.cursor() 

loopChar = ''
while not loopChar == '~':
	make = raw_input("Make: ")
	model = raw_input("Model: ")
	year = raw_input("Year: ")
	color = raw_input("Color: ")
	cylinder = raw_input("Cylinders: ")
	paid = raw_input("Paid: ")
	asking = raw_input("Asking: ")
	loopChar = raw_input("~ to end.")

	cur.execute("insert into lot ( model, make, year, color, cylinder, paid, asking) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(model, make, year, color, cylinder, paid, asking))
	
	abccars.commit()

cur.close()

abccars.close()

