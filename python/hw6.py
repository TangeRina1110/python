def main(x):
    if x[3]== 'HAML':
        return 12
    if x[3]== 'E':
        return 13
    if x[4] == 1993:
        return 6
    if x[4] == 1969:
        if x[0] == 'TOML':
            return 0
        if x[0] == 'DART':
            return ['STON', 'EDN'].index(x[1])+1
        if x[0] == 'NINJA':
            return [1974, 2014, 1992].index(x[2])+3
    if x[4] == 1965:
        if x[2] == 1974:
            return ['TOML', 'DART', 'NINJA'].index(x[0]) + 7
        return [2014, 1992].index(x[2]) + 10

print(main(['TOML', 'STON', 2014, 'GLYPH', 1969]))
print(main(['NINJA', 'STON', 1974, 'HAML', 1969]))
print(main(['DART', 'STON', 2014, 'E', 1969]))
print(main(['DART', 'STON', 2014, 'GLYPH', 1969]))
print(main(['NINJA', 'STON', 1992, 'GLYPH', 1969]))
print(main(['DART', 'EDN', 1974, 'GLYPH', 1965]))


s = ({'GLYPH', 1969, 'TOML'}, {'GLYPH', 1969, 'DART', 'STON'},
     {'GLYPH', 1969, 'DART', 'EDN'}, {'GLYPH', 1969, 'NINJA', 1974},
     {'GLYPH', 1969, 'NINJA', 2014}, {'GLYPH', 1969, 'NINJA', 1992},
     {'GLYPH', 1993}, {'GLYPH', 1965, 1974, 'TOML'},
     {'GLYPH', 1965, 1974, 'DART'}, {'GLYPH', 1965, 1974, 'NINJA'},
     {'GLYPH', 1965, 2014}, {'GLYPH', 1965, 1992}, {'HAML'}, {'E'})


def main(*r):
    s1 = set(r)
    mx = [len(i & s1) for i in s]
    a = [i for i, j in enumerate(mx) if j == max(mx)]
    mn = [len(s[i]) for i in a]
    return a[mn.index(min(mn))]

        
print(main('TOML','STON',2014,'GLYPH',1969))
print(main('NINJA','STON',1974,'HAML',1969))
print(main('DART','STON',2014,'E',1969))
print(main('DART','STON',2014,'GLYPH',1969))
print(main('NINJA','STON',1992,'GLYPH',1969))
