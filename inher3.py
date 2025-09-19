
class A:
    def show(self):
        print("I am class A")

class B(A):
    def show(self):
        print("I am class B")

class C(A):
    def show(self):
        print("I am class C")

class D(B, C):
    pass

# Object of D
obj = D()
obj.show()   # Which 'show()' method will run?

# Checking Method Resolution Order
print(D.__mro__)




