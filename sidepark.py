from Car import Car
import time

def sidepark(car):
	car.steer(25)
	car.gas(-1)
	time.sleep(2.7)

	car.steer(-25)
	car.gas(0)
	time.sleep(2.7)

	car.steer(0)
	car.gas(0.13)
	time.sleep(1)

	car.gas(0)

car = Car()
sidepark(car)