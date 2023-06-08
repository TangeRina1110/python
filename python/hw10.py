import unittest


class MealyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class MealyMachine:
    def __init__(self):
        self.chr = 'A'

    def run(self):
        if self.chr == 'A':
            self.chr = 'B'
            return 0
        elif self.chr == 'C':
            self.chr = 'D'
            return 2
        elif self.chr == 'D':
            self.chr = 'F'
            return 6
        else:
            raise MealyError('run')

    def model(self):
        if self.chr == 'B':
            self.chr = 'C'
            return 1
        elif self.chr == 'D':
            self.chr = 'G'
            return 5
        elif self.chr == 'F':
            self.chr = 'G'
            return 8
        elif self.chr == 'G':
            self.chr = 'H'
            return 10
        else:
            raise MealyError('model')

    def slur(self):
        if self.chr == 'D':
            self.chr = 'D'
            return 4
        elif self.chr == 'F':
            self.chr = 'C'
            return 9
        elif self.chr == 'E':
            self.chr = 'F'
            return 7
        else:
            raise MealyError('slur')

    def draw(self):
        if self.chr == 'D':
            self.chr = 'E'
            return 3
        elif self.chr == 'H':
            self.chr = 'H'
            return 11
        else:
            raise MealyError('draw')


def main():
    return MealyMachine()


def test():
    uni = unittest.TestCase
    # 1
    obj = main()
    assert(obj.run() == 0)
    assert(obj.model() == 1)
    assert(obj.run() == 2)
    assert(obj.slur() == 4)
    assert(obj.draw() == 3)
    assert(obj.slur() == 7)
    assert(obj.model() == 8)
    assert(obj.model() == 10)
    # H
    assert(obj.draw() == 11)
    # 2
    obj = main()
    assert(obj.run() == 0)
    assert(obj.model() == 1)
    assert(obj.run() == 2)
    assert(obj.slur() == 4)
    assert(obj.run() == 6)
    assert(obj.slur() == 9)
    assert(obj.run() == 2)
    assert(obj.draw() == 3)
    assert(obj.slur() == 7)
    assert(obj.slur() == 9)
    assert(obj.run() == 2)
    assert(obj.model() == 5)
    assert(obj.model() == 10)
    # H
    # 3
    obj = main() # A
    with uni.assertRaises(uni, MealyError):
        obj.draw()
    with uni.assertRaises(uni, MealyError):
        obj.model()
    with uni.assertRaises(uni, MealyError):
        obj.slur()
    assert(obj.run() == 0) # B
    with uni.assertRaises(uni, MealyError):
        obj.draw()
    with uni.assertRaises(uni, MealyError):
        obj.slur()
    with uni.assertRaises(uni, MealyError):
        obj.run()
    assert(obj.model() == 1) # C
    with uni.assertRaises(uni, MealyError):
        obj.draw()
    with uni.assertRaises(uni, MealyError):
        obj.model()
    with uni.assertRaises(uni, MealyError):
        obj.slur()
    assert(obj.run() == 2) # D
    assert(obj.draw() == 3) # E
    with uni.assertRaises(uni, MealyError):
        obj.draw()
    with uni.assertRaises(uni, MealyError):
        obj.model()
    with uni.assertRaises(uni, MealyError):
        obj.run()
    assert(obj.slur() == 7) # F
    with uni.assertRaises(uni, MealyError):
        obj.run()   
    with uni.assertRaises(uni, MealyError):
        obj.draw()
    assert(obj.model() == 8) # G
    with uni.assertRaises(uni, MealyError):
        obj.draw()
    with uni.assertRaises(uni, MealyError):
        obj.slur()
    with uni.assertRaises(uni, MealyError):
        obj.run()    
    assert(obj.model() == 10) # H
    with uni.assertRaises(uni, MealyError):
        obj.slur()
    with uni.assertRaises(uni, MealyError):
        obj.run() 
    with uni.assertRaises(uni, MealyError):
        obj.model()


test()
