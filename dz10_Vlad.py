import unittest


class MealyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class MealyMachine:
    def __init__(self):
        self.chr = 'A'

    def debug(self):
        if self.chr == 'A':
            self.chr = 'B'
            return 0
        elif self.chr == 'B':
            self.chr = 'E'
            return 3
        elif self.chr == 'C':
            self.chr = 'D'
            return 4
        elif self.chr == 'F':
            self.chr = 'C'
            return 8
        elif self.chr == 'G':
            self.chr = 'H'
            return 9
        else:
            raise MealyError('debug')

    def join(self):
        if self.chr == 'A':
            self.chr = 'C'
            return 1
        elif self.chr == 'F':
            self.chr = 'G'
            return 7
        elif self.chr == 'G':
            self.chr = 'B'
            return 11
        else:
            raise MealyError('join')

    def warp(self):
        if self.chr == 'B':
            self.chr = 'C'
            return 2
        elif self.chr == 'D':
            self.chr = 'E'
            return 5
        elif self.chr == 'G':
            self.chr = 'D'
            return 10
        elif self.chr == 'E':
            self.chr = 'F'
            return 6
        else:
            raise MealyError('warp')


def main():
    return MealyMachine()


def test():
    uni = unittest.TestCase
    # 1
    obj = main()
    assert(obj.join() == 1)
    assert(obj.debug() == 4)
    assert(obj.warp() == 5)
    assert(obj.warp() == 6)
    assert(obj.join() == 7)
    assert(obj.join() == 11)
    assert(obj.debug() == 3)
    assert(obj.warp() == 6)
    assert(obj.join() == 7)
    assert(obj.debug() == 9)

    # 2
    obj = main()
    assert(obj.debug() == 0)
    # E
    assert(obj.debug() == 3)
    assert(obj.warp() == 6)
    assert(obj.join() == 7)
    # G
    assert(obj.warp() == 10)
    # D
    assert(obj.warp() == 5)
    assert(obj.warp() == 6)
    assert(obj.debug() == 8)
    # C
    assert(obj.debug() == 4)
    assert(obj.warp() == 5)
    assert(obj.warp() == 6)
    assert(obj.join() == 7)
    # G
    assert(obj.join() == 11)
    # B
    assert(obj.warp() == 2)
    # C
    assert(obj.debug() == 4)
    assert(obj.warp() == 5)
    assert(obj.warp() == 6)
    assert(obj.join() == 7)
    assert(obj.debug() == 9)

    # 3
    obj = main()
    # A
    with uni.assertRaises(uni, MealyError):
        obj.warp()
    assert(obj.join() == 1)
    # C
    with uni.assertRaises(uni, MealyError):
        obj.join()
    with uni.assertRaises(uni, MealyError):
        obj.warp()
    assert(obj.debug() == 4)
    # D
    with uni.assertRaises(uni, MealyError):
        obj.debug()
    with uni.assertRaises(uni, MealyError):
        obj.join()
    assert(obj.warp() == 5)
    # E
    with uni.assertRaises(uni, MealyError):
        obj.debug()
    with uni.assertRaises(uni, MealyError):
        obj.join()
    assert(obj.warp() == 6)
    # F
    with uni.assertRaises(uni, MealyError):
        obj.warp()
    assert(obj.join() == 7)
    # G
    assert(obj.join() == 11)
    # B
    with uni.assertRaises(uni, MealyError):
        obj.join()
    assert(obj.debug() == 3)
    # E
    assert(obj.warp() == 6)
    assert(obj.join() == 7)
    assert(obj.debug() == 9)


test()
