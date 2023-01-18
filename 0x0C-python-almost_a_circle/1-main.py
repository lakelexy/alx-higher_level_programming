#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(1, 2, 0, 0, 12)
    print('id =', r3.id, 'width =', r3.width)

    r4 = Rectangle(123, 4)
    print(r4.id)
