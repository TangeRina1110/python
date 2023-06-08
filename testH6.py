'''def dart_ninja(x, left, middle, right):
    if x[0] == 'DART':
        return middle
    if x[0] == 'NINJA':
        return right
    return left
    
def one(x, left, right):
    if x[1] == 'STON':
        return left
    return right
def two(x, left, middle, right):
    if x[2] == 1974:
        return left
    if x[2] == 2014:
        return middle
    return right



def main(x):
    if x[3] == 'GLYPH':
        if x[4] == 1969:
            return dart_ninja(x, 0, one(x, 1, 2), two(x, 3, 4, 5)) 
        if x[4] == 1965:
            return two(x, dart_ninja(x, 7, 8, 9), 10, 11)
        return 6
    if x[3] == 'HAML':
        return 12
    return 13


print(main(['TOML', 'STON', 2014, 'GLYPH', 1969]))
print(main(['NINJA', 'STON', 1974, 'HAML', 1969]))
print(main(['DART', 'STON', 2014, 'E', 1969]))
print(main(['DART', 'STON', 2014, 'GLYPH', 1969]))
print(main(['NINJA', 'STON', 1992, 'GLYPH', 1969]))
print(main(['DART', 'EDN', 1974, 'GLYPH', 1965]))
print(main(['NINJA', 'STON', 2014, 'GLYPH', 1969]))'''


'''def lfe(x, left, right): #16
    if x[0] == 'LFE':
        return left
    return right
def one(x, left, right):
    if x[1] == 1961:
        return left
    return right
def four(x, left, right):
    if x[4] == 'SMT':
        return left
    return right
def two(x, left, right):
    if x[2] == 'TCL':
        return left
    return right

def main(x):
    if x[3] == 'X10':
        return lfe(x, four(x, 0, 1), 2)
    if x[3] == 'COQ':
        return lfe(x, two(x, one(x, 3, 4), 5), 6)
    if x[3] == 'ELM':
        return one(x, four(x, two(x, 7, 8), 9), 10)

print(main(['LFE', 1998, 'TCL', 'COQ', 'NIX'])) #= 4
print(main(['ABNF', 1998, 'TCL', 'ELM', 'SMT'])) #= 10
print(main(['ABNF', 1961, 'YANG', 'COQ', 'SMT'])) #= 6
print(main(['LFE', 1998, 'TCL', 'X10', 'NIX'])) #= 1
print(main(['ABNF', 1998, 'TCL', 'X10', 'NIX'])) #= 2'''

'''def four(x, left, right): #27
    if x[4] == 1974:
        return left
    return right
def noll(x, left, right):
    if x[0] == 1993:
        return left
    return right
def one(x, left, middle, right):
    if x[1] == 1991:
        return left
    if x[1] == 1981:
        return middle
    return right
def three(x, left, middle, right):
    if x[3] == 'GLSL':
        return left
    if x[3] == 'TLA':
        return middle
    return right

def main(x):
    if x[2] == 'RDOC':
        return four(x, noll(x, one(x, 0, 1, 2), one(x, 3, 4, 5)), one(x, three(x, 6, 7, 8), 9, 10))
    if x[2] == 'STAN':
        return 11
    return 12

print(main([1988, 1991, 'JFLEX', 'ADA', 1974]))# = 12
print(main([1993, 1991, 'STAN', 'ADA', 1974]))# = 11
print(main([1993, 1961, 'RDOC', 'TLA', 1974]))# = 2
print(main([1993, 1991, 'RDOC', 'GLSL', 2005]))# = 6
print(main([1988, 1981, 'RDOC', 'TLA', 2005]))# = 9'''

'''def three(x, left, right): #var30 01-21
    if x[3] == 'ROFF':
        return left
    return right
def noll(x, left, middle, right):
    if x[0] == 2002:
        return left
    elif x[0] == 1964:
        return middle
    return right
def one(x, left, middle, right):
    if x[1] == 1976:
        return left
    if x[1] == 1962:
        return middle
    return right
def two(x, left, right):
    if x[2] == 'XOJO':
        return left
    return right


def main(x):
    if x[4] == 'TEX':
        return three(x, one(x, 0, two(x, 1, 2), 3), 4)
    return noll(x, three(x, two(x, 5, 6), one(x, 7, 8, 9)), 10, 11)


print(main([2002, 1962, 'EQ', 'KIT', 'TEX'])) #= 4
print(main([2013, 1976, 'XOJO', 'ROFF', 'TEX'])) #= 0
print(main([1964, 1976, 'XOJO', 'KIT', 'TXL'])) #= 10
print(main([1964, 1962, 'EQ', 'ROFF', 'TEX'])) #= 2
print(main([1964, 1962, 'XOJO', 'ROFF', 'TEX']))# = 1'''

'''def noll(x, left, right):
    if x[0] == 'LFE':
        return left
    return right
def one(x, left, right):
    if x[1] == 1961:
        return left
    return right
def two(x, left, right):
    if x[2] == 'TCL':
        return left
    return right
def four(x, left, right):
    if x[4] == 'SMT':
        return left
    return right


def main(x):
    if x[3] == 'X10':
        return noll(x, four(x, 0, 1), 2)
    if x[3] == 'COQ':
        return noll(x, two(x, one(x, 3, 4), 5), 6)
    return one(x, four(x, two(x, 7, 8), 9), 10)


print(main(['LFE', 1998, 'TCL', 'COQ', 'NIX']))
print(main(['ABNF', 1998, 'TCL', 'ELM', 'SMT']))
print(main(['ABNF', 1961, 'YANG', 'COQ', 'SMT']))
print(main(['LFE', 1998, 'TCL', 'X10', 'NIX']))
print(main(['ABNF', 1998, 'TCL', 'X10', 'NIX']))
'''

'''def noll(x, left, middle, right):
    if x[0] == 'BISON':
        return left
    if x[0] == 'POD':
        return middle
    return right
def one(x, left, middle, right):
    if x[1] == 1968:
        return left
    if x[1] == 1957:
        return middle
    return right
def two(x, left, right):
    if x[2] == 1965 :
        return left
    return right

def main(x):
    if x[3] == 'CLICK':
        return two(x, noll(x, 0, 1, 2), noll(x, 3, 4, 5))
    return two(x, 6, one(x, 7, 8, 9))

print(main(['POD', 1991, 1965, 'NIT']))
print(main(['POD', 1957, 1975, 'CLICK']))
print(main(['SLIM', 1968, 1975, 'CLICK']))
print(main(['BISON', 1968, 1965, 'CLICK']))
print(main(['POD', 1957, 1975, 'NIT']))'''

'''def noll(x, left, middle, right): #var40
    if x[0] == 1987:
        return left
    if x[0] == 1972:
         return middle
    return right

def one(x, left, right):
    if x[1] == 1986:
        return left
    return right
def two(x, left, right):
    if x[2] == 'PONY':
        return left
    return right

def main(x):
    if x[3] == 'LOGOS':
        return two(x, noll(x, 0, 1, 2), 3)
    if x[3] == 'TEX':
        return noll(x, one(x, 4, 5), one(x, 6, 7), 8)
    return 9

print(main([1979, 1986, 'SASS', 'TEX']))
print(main([1979, 1986, 'SASS', 'LOGOS']))
print(main([1972, 2015, 'PONY', 'LOGOS']))
print(main([1972, 1986, 'SASS', 'TEX']))
print(main([1972, 2015, 'SASS', 'OCAML']) )'''
