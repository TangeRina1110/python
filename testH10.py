'''import unittesr


class MealyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Mealy:
    def __init__(self):
        self.chr = 'A'
        
    def debug(self):
        if self.chr == 'A':
            self.chr = 'B'
            return 0
        elif selr.chr == 'B':
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
            return (MealyError('debug'))
        
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
            return (MealyError('join'))

    def warp(self):
        if self.chr == 'B':
            self.chr = 'C'
            return 2
        elif self.chr == 'E':
            self.chr = 'F'
            return 6
        elif self.chr == 'D':
            self.chr = 'E'
            return 5
        elif self.chr == 'G':
            self.chr = 'D'
            return 10
        else:
            return (MealyException('warp'))

def main():
    return Mealy()

def test():
    uni = unittest.TestCase
    #1
    obj = main()
    assert(obj.join() == 1)'''

'''import unittest

class MealyError(Ecept):
    def __init__(self, mes):
        self.mes = mes
        super().__init__(mes)


class Mealy(self):
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
        elif sel.chr == 'G':
            self.chr = 'H'
            return 10
        else:
            raise MealyError('grow')
            
def main():
    return Mealy()
def test():
    uni = unitest.Testcase
    #1
    obj = main()
    assert(obj.fill() == 0)
    assert(obj.leer() == 4)
    assert(obj.crush() == 5)
    assert(obj.grow() == 7)
    assert(obj.crush() == 8)
    assert(obj.leer() == 9)
    assert(obj.grow() == 10)
    assert(obj.crush() == 11)
    #2
    obj = main()
    assert(obj.leer() == 1)
    assert(obj.fill() == 0)
    assert(obj.leer() == 4)
    # to A
    assert(obj.grow() == 6)
    assert(obj.leer() == 1)'''

'''class MealyError(Except):
    pass


class Mealy:
    def __init__(self):
        self.chr = 'A'

    def run(self):
        if self.chr == 'A':
            self.chr = 'B'
            return 0
        elif self.chr == 'c':
            self.chr = 'D'
            return 2
        elif self.chr == 'D':
            self.chr = 'F'
            return 6
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
        raise MealyError('model')

    def draw(self):
        if self.chr == 'D':
            self.chr = 'E'
            return 3
        elif self.chr == 'H':
            self.chr = 'H'
            return 11
        raise MealyError('draw')

    def slur(self):
        if self.chr == 'D':
            self.chr = 'D'
            return 4
        elif self.chr == 'E':
            self.chr = 'F'
            return 7
        elif self.chr == 'F':
            self.chr = 'C'
            return 9
        raise MealyError('slur')


def main():
    return Mealy()


def raises(f, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def tast():
    o = main()
    assert o.run() == 0
    assert o.model() == 1
    assert o.run() == 2
    assert o.slur() == 4
    assert o.draw() == 3
    assert o.slur() == 7
    assert o.slur() == 9
    assert o.run() == 2
    assert o.slur() == 4
    assert o.run() == 6
    assert o.model() == 8
    assert o.model() == 10
    assert o.draw() == 11
    o = main()
    assert o.run() == 0
    assert o.model() == 1
    assert o.run() == 2
    assert o.slur() == 4
    assert o.model() == 5
    assert o.model() == 10
    raises(lambda: o.slur(), MealyError)
    raises(lambda: o.model(), MealyError)
    raises(lambda: o.run(), MealyError)
    raises(lambda: o.draw(), MealyError)'''
    

import unittest


class MealyError(Exception):
    pass

class Mealy:
    def __init__(self):
        self.chr = 'A'

    def slog(self):
        if self.chr == 'A':
           self.chr = 'B'
           return 0
        if self.chr == 'B':
            self.chr = 'C'
            return 1
        if self.chr == 'D':
            self.chr = 'E'
            return 5
        if self.chr == 'E':
            self.chr = 'F'
            return 6
        if self.chr == 'F':
            self.chr = 'G'
            return 8
        if self.chr == 'G':
            self.chr = 'H'
            return 10
        raise MealyError('slog')

    def stop(self):
        if self.chr == 'B':
            self.chr = 'E'
            return 2
        if self.chr == 'C':
            self.chr = 'D'
            return 4
        if self.chr == 'E':
            return 7
        if self.chr == 'G':
            self.chr = 'E'
            return 11
        raise MealyError('stop')

    def cast(self):
        if self.chr == 'B':
            self.chr = 'G'
            return 3
        if self.chr == 'F':
            self.chr = 'B'
            return 9
        raise MealyError('cast')
        

def main():
    return Mealy()

def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None

def test():
    obj = main()
    assert obj.slog() == 0
    assert obj.slog() == 1
    assert obj.stop() == 4
    assert obj.slog() == 5
    assert obj.stop() == 7
    assert obj.slog() == 6
    assert obj.cast() == 9
    assert obj.stop() == 2
    assert obj.stop() == 7
    assert obj.slog() == 6
    assert obj.cast() == 9
    assert obj.cast() == 3
    assert obj.stop() == 11
    assert obj.stop() == 6
    assert obj.slog() == 8
    assert obj.slog() == 10
    raises(lambda: obj.cast(), MealyError)
    raises(lambda: obj.stop(), MealyError)
    raises(lambda: obj.slog(), MealyError)
    


    
