from abc import ABC, abstractmethod
from typing import List, Protocol


class MyProtocol(Protocol):
    def my_method(self, arg: int) -> None:
        pass

class MyAbstractClass(ABC):
    @abstractmethod
    def my_method(self, arg: int) -> None:
        pass

class MyConcreteClass1(MyAbstractClass):
    def my_method(self, arg: int) -> None:
        print(f"MyConcreteClass1 with arg: {arg}")

class MyConcreteClass2:
    def my_method(self, arg: int) -> None:
        print(f"MyConcreteClass2 with arg: {arg}")

def my_function(obj: MyProtocol, arg: int) -> None:
    obj.my_method(arg)

# MyConcreteClass1 is a valid argument because it conforms to MyAbstractClass
my_function(MyConcreteClass1(), 5) # prints "MyConcreteClass1 with arg: 5"

# MyConcreteClass2 is a valid argument because it conforms to MyProtocol
my_function(MyConcreteClass2(), 7) # prints "MyConcreteClass2 with arg: 7"

my_list: List[MyProtocol] = [MyConcreteClass2()] # MyConcreteClass2 is a valid element of the list because it conforms to MyProtocol

