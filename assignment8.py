class A:
    def __init__(self, a, b, c):
        self.__a = a  # Private member
        self._b = b  # Protected member
        self.c = c  # Public member
    
    def display(self):
        try:
            print("Values in class A:")
            print("a:", self.__a)  # Accessing private member
        except AttributeError:
            print("Private member 'a' cannot be accessed.")
        else:
            print("b:", self._b)
            print("c:", self.c)


class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    
    def display(self):
        super().display()
        print("Values in class B:")
        print("a:", self._A__a)  # Accessing private member of class A using name mangling
        print("b:", self._b)
        print("c:", self.c)


# Create an instance of class B
obj_b = B(1, 2, 3)

# Call the display method to see the behavior
obj_b.display()
