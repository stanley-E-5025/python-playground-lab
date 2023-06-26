"""
The script creates a CarBuilder class that adds functionalities to a provided CarFactory class. 
It uses asyncio library to run multiple cars acceleration, stop and showing the metrics of cars in parallel. 
Each car has attributes gasoline & speed_per_second and each car stops after a random time.
"""

import asyncio
import random


class CarBuilder:
    def __init__(self, factory):
        self.factory = factory

    async def accelerate(self, car_type, gasoline, speed_per_second):
        car = self.factory.create_car(car_type)
        car.gasoline = gasoline
        car.speed_per_second = speed_per_second
        while car.gasoline > 0:
            await asyncio.sleep(1)
            car.gasoline -= car.speed_per_second / 10
            print(f"The {car.type} is now going {car.speed_per_second} km/h and has {car.gasoline} L of gasoline left.")
        print(f"The {car.type} has run out of gasoline.")

    async def stop(self, car_type):
        car = self.factory.create_car(car_type)
        random_time = random.randint(1, 10)
        await asyncio.sleep(random_time)
        print(f"The {car.type} has stopped after {random_time} seconds.")

    async def show_metrics(self, car_type):
        car = self.factory.create_car(car_type)
        print(f"The {car.type} has {car.gasoline} L of gasoline left and is going {car.speed_per_second} km/h.")


class CarFactory:
    def create_car(self, car_type):
        if car_type == "sedan":
            return Sedan()
        elif car_type == "hatchback":
            return Hatchback()
        elif car_type == "suv":
            return SUV()


class Sedan:
    def __init__(self):
        self.num_wheels = 4
        self.type = "sedan"
        self.gasoline = 0
        self.speed_per_second = 0


class Hatchback:
    def __init__(self):
        self.num_wheels = 4
        self.type = "hatchback"
        self.gasoline = 0
        self.speed_per_second = 0


class SUV:
    def __init__(self):
        self.num_wheels = 4
        self.type = "suv"
        self.gasoline = 0
        self.speed_per_second = 0


factory = CarFactory()
builder = CarBuilder(factory)


async def run():
    await asyncio.gather(
        builder.accelerate("sedan", 50, 80),
        builder.accelerate("hatchback", 35, 60),
        builder.accelerate("suv", 60, 100),
    )
    await asyncio.gather(
        builder.stop("sedan"),
        builder.stop("hatchback"),
        builder.stop("suv"),
    )
    await asyncio.gather(
        builder.show_metrics("sedan"),
        builder.show_metrics("hatchback"),
        builder.show_metrics("suv"),
    )


asyncio.run(run())
