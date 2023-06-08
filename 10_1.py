class MealyError(Exception):
    pass


class Milya:
    state = "A"

    def base(self):
        if self.state == "A":
            self.state = "B"
            return 0
        elif self.state == "B":
            self.state = "C"
            return 2
        elif self.state == "F":
            self.state = "F"
            return 9
        elif self.state == "G":
            self.state = "B"
            return 11
        else:
            raise MealyError("base")

    def run(self):
        if self.state == "A":
            self.state = "C"
            return 1
        elif self.state == "C":
            self.state = "D"
            return 4
        elif self.state == "E":
            self.state = "F"
            return 6
        elif self.state == "F":
            self.state = "H"
            return 8
        else:
            raise MealyError("run")

    def walk(self):
        if self.state == "B":
            return 3
        elif self.state == "D":
            self.state = "E"
            return 5
        elif self.state == "F":
            self.state = "G"
            return 7
        elif self.state == "G":
            self.state = "H"
            return 10
        else:
            raise MealyError("walk")


def test():
    o = main()
    # A-C-D-E-F-F-H
    try:
        o.walk()
    except MealyError:
        pass
    o.run()
    try:
        o.base()
    except MealyError:
        pass
    o.run()
    try:
        o.run()
    except MealyError:
        pass
    o.walk()
    o.run()
    o.base()
    o.run()
    # A-C-D-E-F-H
    o = main()
    o.run()
    o.run()
    o.walk()
    o.run()
    o.run()
    # A-C-D-E-F-G-H
    o = main()
    o.run()
    o.run()
    o.walk()
    o.run()
    o.walk()
    o.walk()
    # A-B-B-C-D-E-F-F-G-H
    o = main()
    o.base()
    o.walk()
    o.base()
    o.run()
    o.walk()
    o.run()
    o.base()
    o.walk()
    o.walk()
    # A-B-B-C-D-E-F-F-H
    o = main()
    o.base()
    o.walk()
    o.base()
    o.run()
    o.walk()
    o.run()
    o.base()
    o.run()
    # A-B-C-D-E-F-G-B-C-D-E-F-G-H
    o = main()
    o.base()
    o.base()
    o.run()
    o.walk()
    o.run()
    o.walk()
    o.base()
    o.base()
    o.run()
    o.walk()
    o.run()
    o.walk()
    o.walk()
    # A-B-C-D-E-F-G-B-C-D-E-F-H
    o = main()
    o.base()
    o.base()
    o.run()
    o.walk()
    o.run()
    o.walk()
    o.base()
    o.base()
    o.run()
    o.walk()
    o.run()
    o.run()


def main():
    o = Milya()
    return o


test()
