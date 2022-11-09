"""Method Overloading"""
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            s = a+b+c
        elif a != None and b != None:
            s = a+b
        elif a != None:
            s = a
        return s

s1 = Student(53, 57)
print(s1.sum(1, 4))


"""Method Overriding"""
class A:
    def show(self):
        print("In A show() ")
class B(A):
    def show(self):
        print("In B show()")

a1 = A()
a1.show()
b1 = B()
b1.show()


"""Operator Overloading"""
class Book:
    def __init__(self,price):
        self.price = price
    def __add__(self,other):
        return self.price + other.price
    def __lt__(self,other):
        return self.price < other.price
book1 = Book(10)
book2 = Book(20)
total_price = book1 + book2
compare = book1 < book2
print(total_price)
print(compare)