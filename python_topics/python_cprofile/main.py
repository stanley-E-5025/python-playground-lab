"""
In this example, we first defined a class MyClass which contains three methods my_function1, my_function2, my_function3 which we want to profile.

Then we define two utility functions profile_class and profile_function which takes class or function and some arguments, and these utility functions uses cProfile.Profile() to create a profiler object, enable it, execute the class or function and then disable it.

In the main method, we are using these utility functions first for the MyClass and then for the function my_function3. In each case, we use the pstats module to create a human-readable report of the profiling information.
"""

import cProfile
import pstats


class MyClass:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def my_function1(self):
        res = 0
        for i in range(1000):
            res += i

    def my_function2(self):
        res = 1
        for i in range(1000):
            res *= i

    def my_function3(self):
        res = 0
        for i in range(10):
            res += i
        return res


def profile_class(cls, *args, **kwargs):
    """
    Profiles all methods in the given class
    """
    profiler = cProfile.Profile()
    profiler.enable()
    instance = cls(*args, **kwargs)
    for method in [getattr(instance, x) for x in dir(instance) if callable(getattr(instance, x)) and not x.startswith("__")]:
        method()
    profiler.disable()
    return profiler


def profile_function(fn, *args, **kwargs):
    """
    Profiles the given function
    """
    profiler = cProfile.Profile()
    profiler.enable()
    fn(*args, **kwargs)
    profiler.disable()
    return profiler


if __name__ == "__main__":
    # Profile the class
    cls_profiler = profile_class(MyClass, 1, 2)
    stats = pstats.Stats(cls_profiler)
    stats.strip_dirs().sort_stats("tottime").print_stats()

    # Profile the function my_function3
    instance = MyClass(1, 2)
    function3_profiler = profile_function(instance.my_function3)
    stats = pstats.Stats(function3_profiler)
    stats.strip_dirs().sort_stats("tottime").print_stats()
