# -*- encoding: utf-8 -*-

class basis:

    def __init__(self, num : int) -> None:
        self._Num = num     # a number to differentiate between all the instances of this class

    def __str__(self) -> str:
        return "Test-Object of class t%i"%self._Num
    
    def switch(self, new_class) -> None:
        self_new = new_class()
        self.__class__ = self_new.__class__
        self.__dict__ = self_new.__dict__

class t1(basis):

    def __init__(self) -> None:
        super().__init__(1)

    def function_only_in_t1(self) -> None:
        print("\tthis can only be called from t1")

class t2(basis):

    def __init__(self) -> None:
        super().__init__(2)
    
    def function_only_in_t2(self) -> None:
        print("\tthis can only be called from t2")


#------- test -------

test_object = t1()

print("Test-object initialized: %s"%test_object)

test_object.switch(t2)

print("Test-object after switching to t2: %s"%test_object)
print("Calling function from t2: ")
test_object.function_only_in_t2()

test_object.switch(t1)

print("Test-object after switching to t1: %s"%test_object)
print("Calling function from t1: ")
test_object.function_only_in_t1()