import unittest


class MealyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class MealyMachine:
    def __init__(self):
        self.chr = 'A'

    def leer(self):
        if self.chr == 'A':
            self.chr = 'A'
            return 1
        elif self.chr == 'B':
            self.chr = 'C'
            return 4
        elif self.chr == 'F':
            self.chr = 'G'
            return 9
        else:
            raise MealyError('leer')

    def fill(self):
        if self.chr == 'A':
            self.chr = 'B'
            return 0
        else:
            raise MealyError('fill')

    def crush(self):
        if self.chr == 'A':
            self.chr = 'H'
            return 3
        elif self.chr == 'C':
            self.chr = 'D'
            return 5
        elif self.chr == 'E':
            self.chr = 'F'
            return 8
        elif self.chr == 'H':
            self.chr = 'E'
            return 11
        else:
            raise MealyError('crush')

    def grow(self):
        if self.chr == 'A':
            self.chr = 'F'
            return 2
        elif self.chr == 'C':
            self.chr = 'A'
            return 6
        elif self.chr == 'D':
            self.chr = 'E'
            return 7
        elif self.chr == 'G':
            self.chr = 'H'
            return 10
        else:
            raise MealyError('grow')


def main():
    return MealyMachine()


def test():
    uni = unittest.TestCase
    # 1
    obj = main()
    assert(obj.fill() == 0)
    assert(obj.leer() == 4)
    assert(obj.crush() == 5)
    assert(obj.grow() == 7)
    assert(obj.crush() == 8)
    assert(obj.leer() == 9)
    assert(obj.grow() == 10)
    # H
    assert(obj.crush() == 11)

    # 2
    obj = main()
    assert(obj.leer() == 1)
    assert(obj.fill() == 0)
    assert(obj.leer() == 4)
    # to A
    assert(obj.grow() == 6)
    assert(obj.leer() == 1)
    # from A
    assert(obj.fill() == 0)
    assert(obj.leer() == 4)
    # to D
    assert(obj.crush() == 5)
    assert(obj.grow() == 7)
    assert(obj.crush() == 8)
    assert(obj.leer() == 9)
    assert(obj.grow() == 10)
    # H
    assert(obj.crush() == 11)
    assert(obj.crush() == 8)
    assert(obj.leer() == 9)
    assert(obj.grow() == 10)
    # H
    assert(obj.crush() == 11)

    # 3
    obj = main()
    assert(obj.leer() == 1)
    assert(obj.fill() == 0)
    assert(obj.leer() == 4)
    # to A
    assert(obj.grow() == 6)
    # from A
    assert(obj.grow() == 2)
    # to F
    assert(obj.leer() == 9)
    assert(obj.grow() == 10)
    # H
    assert(obj.crush() == 11)
    assert(obj.crush() == 8)

    # 4
    obj = main()
    assert(obj.leer() == 1)
    assert(obj.fill() == 0)
    assert(obj.leer() == 4)
    # to A
    assert(obj.grow() == 6)
    # from A
    assert(obj.crush() == 3)
    # to H
    assert(obj.crush() == 11)
    assert(obj.crush() == 8)
    assert(obj.leer() == 9)
    assert(obj.grow() == 10)

    # 5
    obj = main()
    assert(obj.leer() == 1)
    assert(obj.fill() == 0)
    with uni.assertRaises(uni, MealyError):
        obj.grow()
    with uni.assertRaises(uni, MealyError):
        obj.fill()
    with uni.assertRaises(uni, MealyError):
        obj.crush()
    assert(obj.leer() == 4)
    with uni.assertRaises(uni, MealyError):
        obj.fill()
    with uni.assertRaises(uni, MealyError):
        obj.leer()
    # to A
    assert(obj.grow() == 6)
    assert(obj.leer() == 1)
    # from A
    assert(obj.fill() == 0)
    assert(obj.leer() == 4)
    # to D
    assert(obj.crush() == 5)
    with uni.assertRaises(uni, MealyError):
        obj.fill()
    with uni.assertRaises(uni, MealyError):
        obj.leer()
    with uni.assertRaises(uni, MealyError):
        obj.crush()
    assert(obj.grow() == 7)
    with uni.assertRaises(uni, MealyError):
        obj.grow()
    with uni.assertRaises(uni, MealyError):
        obj.fill()
    with uni.assertRaises(uni, MealyError):
        obj.leer()
    assert(obj.crush() == 8)
    with uni.assertRaises(uni, MealyError):
        obj.grow()
    with uni.assertRaises(uni, MealyError):
        obj.fill()
    with uni.assertRaises(uni, MealyError):
        obj.crush()
    assert(obj.leer() == 9)
    with uni.assertRaises(uni, MealyError):
        obj.leer()
    with uni.assertRaises(uni, MealyError):
        obj.fill()
    with uni.assertRaises(uni, MealyError):
        obj.crush()
    assert(obj.grow() == 10)
    with uni.assertRaises(uni, MealyError):
        obj.grow()
    with uni.assertRaises(uni, MealyError):
        obj.fill()
    with uni.assertRaises(uni, MealyError):
        obj.leer()
    # H
    assert(obj.crush() == 11)


test()
