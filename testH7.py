'''def main(h):
    v = int(h,16)
    v_bin = bin(v)[2:].zfill(36)
    k1 = v & 63
    k3 = (v >> 9) & 255
    k4 = (v >> 17) & 511
    k5 = (v >> 26) & 127
    k6 = (v >> 33) & 7
    d = k6 | (k3 << 6) | (k1 << 14) | (k5 << 20) | (k4 << 27)
    num = hex(d)
    return str(num)

print(main('0x74542b298'))
print(main('0x4391d7d9f'))
print(main('0x1265b7ae8'))
print(main('0x6b6feea0c'))'''

'''def main(i): #30ИМБО-01-21
    x1 = 0b11 & i
    x2 = 0b111111 &(i>>2)
    x3 = 0b111111111 & (i>>8)
    x4 = 0b111 & (i>>17)
    return [('X1', x1),('X2', x2),('X3' x3),('X4', x4)]
print (main(370451))'''

'''def main(i):
    v = int(i, 16)
    v1 = 0b111111 & v
    v3 = 0b11111111 & (v >> 9)
    v4 = 0b111111111 & (v >> 17)
    v5 = 0b1111111 & (v >> 26)
    v6 = 0b111 & (v >> 33)
    v_res = v6 | v3 << 6 | v1 << 14 | v5 << 20 | v4 << 27
    num = hex(v_res)
    return str(num)

print(main('0x74542b298'))'''

'''def main(i): #var2
    t1 = 0b1 & i
    t2 = 0b1111111 & (i >> 1)
    t3 = 0b111 & (i >> 8)
    t4 = 0b11 & (i >> 11)
    t5 = 0b1 & (i >> 13)
    t6 = 0b1111 & (i >> 14)
    return tuple(map(str,(hex(t1),hex(t2),hex(t3), hex(t4), hex(t5), hex(t6))))
print( main(33102))'''


'''def main(i): #var3
    x = []
    for elem in i:
        elem = int(elem, 16)
        x.append(elem)
    num = x[0] | x[1]<< 5 | x[2] << 11 | x[3] << 13
    return num

print(main(('0x6', '0x30', '0x3', '0x3')))
print(main(('0x3', '0x2', '0x0', '0xa')))'''

'''def main(i):
    n = []
    for x in i:
        t = False
        for j in x:
            if t == True:
                elem = int(j, 16)
                n.append(elem)
            t = True
    print(n)
    num = hex(n[0] | n[1] << 2| n[2] << 4| n[3] << 8 |n[4] << 19) 
           
    return num

print(main([('S1', '0x1'), ('S2', '0x0'), ('S3', '0x4'), ('S4', '0x1'), ('S6', '0x1')]))
'''

'''def main(i):
    k1 = 0b111111111 & i
    k3 = 0b11 & (i >> 15)
    k4 = 0b111 &(i >> 17)
    k5 = 0b11111111 &(i>>20)
    return tuple(map(int, (k1, k3, k4, k5)))
print(main(87805285))'''

'''def main(i):
    v = int(i, 16)
    v1 = 0b111111111 & v
    v2 = 0b11111111 & (v>>9)
    v3 = 0b1 &(v>>17)
    v4 = 0b1 &(v>>18)
    v5 = 0b1 &(v>>19)
    num = [('v1', str(v1)), ('v2', str(v2)), ('v3', str(v3)), ('v4', str(v4)), ('v5', str(v5))]
    return num

print(main('0xfcb8c'))
print(main('0x1b8fd'))
print(main('0xa994a'))
print(main('0x59592'))'''

'''def main(i): #var16
    q1 = 0b1 & i
    q3 = 0b11111111 & (i >> 7)
    q4 = 0b111111111 & (i>> 15)
    res = q3 | q4 << 8 | q1 <<23
    return res

print(main(14004953))'''

'''def main(i): #var3
    x = []
    for elem in i:
        elem = int(elem, 16)
        x.append(elem)
    num = x[0] | x[1]<< 5 | x[2] << 11 | x[3] << 13
    return num

print(main(('0x6', '0x30', '0x3', '0x3')))
print(main(('0x3', '0x2', '0x0', '0xa')))'''

'''def main(i):
    x = []
    for n in i:
        x.append(n)
    num = x[0] | x[1] << 5 | x[2] << 6 | x[3] << 11
    return num
print(main((25, 1, 1, 32)))'''


'''def main(x): #var40
    o = int(x, 16)
    o1 = 0b111 & o
    o2 = 0b1111111111 & (o >> 3)
    o3 = 0b11 & (o >> 13)
    o4 = 0b1111 & (o >> 15)
    return ([('O1', o1), ('O2', o2), ('O3', o3), ('O4', o4)])

print(main('0x2f930'))
print(main('0x7178b'))
print(main('0x5aae6'))
print(main('0x3dd74'))'''
    
    
