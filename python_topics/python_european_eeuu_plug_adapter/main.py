import time
from abc import ABC, abstractmethod

# <----------------------------------------CLASS1----------------------------------------> #


class IUkPlug(ABC):
    @staticmethod
    @abstractmethod
    def electricity_220v():
        """electricity supply"""


class UkPlug(IUkPlug):
    def electricity_220v(self):
        time.sleep(1)
        print("220 Volt")


# <----------------------------------------CLASS2----------------------------------------> #


class IUsPlug(ABC):
    @staticmethod
    @abstractmethod
    def electricity_110v():
        """electricity supply"""


class UsPlug(IUsPlug):
    def electricity_110v(self):
        time.sleep(1)
        print("110 Volt")


# <----------------------------------------ADAPTER----------------------------------------> #


class UktoUsAdapter(IUkPlug):
    def __init__(self):
        self.us_Plug = UsPlug()

    def electricity_220v(self):
        time.sleep(2)
        print("You are using a EEUU adapter")
        self.us_Plug.electricity_110v()


# <----------------------------------------CLIENT_CODE----------------------------------------> #


# EUROPEAN PLUG VOL

my_plug_uk = UkPlug()
my_plug_uk.electricity_220v()


# EEUU PLUG VOL
my_plug_us = UsPlug()
my_plug_us.electricity_110v()


# ERROR CASE

try:
    print("<=====================USING_UK_WITHOUT_ADAPTER=====================>")
    my_plug_uk = UkPlug()
    my_plug_uk.electricity_110v()
except AttributeError:
    print("you need an adapter to use EURO plug in EEUU 🔌")


finally:
    print("<=====================USING_UK_WITH_ADAPTER=====================>")

    my_adapter_to_eeuu = UktoUsAdapter()
    my_adapter_to_eeuu.electricity_220v()
