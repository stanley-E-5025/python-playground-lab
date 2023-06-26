from abc import ABC, abstractmethod

# Create an abstract class (basic calculator) for an example only.


class Calculation(ABC):

    # Abstracts the method with the decorator @abstractmethod
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass

    def multiply(self):
        pass

    def division(self):
        pass


# Create a class that uses our abstraction-based class (ABC) as a parameter.


class Calculator(Calculation):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # These functions follow the structure that we declared in our (ABC)
    def add(self):
        print(self.a + self.b)

    def subtract(self):
        print(self.a - self.b)


def main():
    take = Calculator(10, 5)
    take.add()
    take.subtract()

    return


if __name__ == "__main__":
    main()
