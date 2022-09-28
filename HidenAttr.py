class Parent:
    var_1 = 12
    _var_2 = 13
    __var_3 = 14

    def __init__(self):
        self.ivar_1 = 22
        self._ivar_2 = 23
        self.__ivar_3 = 24

    def parent_method(self):
        print(self.var_1)
        print(self._var_2)
        print(self.__var_3)
        print(self.ivar_1)
        print(self._ivar_2)
        print(self.__ivar_3)

class Child(Parent):
    def child_method(self):
        print(self.var_1)
        print(self._var_2)
        # print(self.__var_3) не даст
        print(self.ivar_1)
        print(self._ivar_2)
        # print(self.__ivar_3) не даст

obj = Child()
# obj.parent_method()
obj.child_method()