from struct import unpack


def main(obj):
    result = {}
    b_struct_address = unpack('>L', obj[5:9])[0]

    result['A1'] = parse_b(obj, address=b_struct_address)  # структура B
    result['A2'] = unpack('>q', obj[9:17])[0]  # int64
    result['A3'] = [i for i in unpack('>BB', obj[17:19])]  # массив uint8 размера 2
    return result


def parse_b(obj, address):  # разбор структуры b
    result = {}
    start = address
    result['B1'] = unpack('>f', obj[start:start + 4])[0]  # float
    result['B2'] = unpack('>l', obj[start + 4:start + 8])[0]  # int32
    result['B3'] = {  # массив структур C
        'C1': unpack('>h', obj[start + 8:start + 10])[0],
        'C2': unpack('>Q', obj[start + 10:start + 18])[0]
    }

    # подготовка к обработке массива структур D
    d_struct_arr_sz = unpack('>H', obj[start + 18:start + 20])[0]
    d_struct_arr_addr = unpack('>L', obj[start + 20:start + 24])[0]
    d_struct_lst = []
    for i in range(d_struct_arr_sz):
        d_struct_addr = unpack('>H', obj[d_struct_arr_addr:d_struct_arr_addr + 2])[0]
        d_struct_lst.append(parse_d(obj, d_struct_addr))
        d_struct_arr_addr += 2
    result['B4'] = d_struct_lst  # список структур D
    result['B5'] = [i for i in unpack('>qqqq', obj[start + 24:start + 56])]  # массив int64
    result['B6'] = unpack('>L', obj[start + 56:start + 60])[0]
    return result


def parse_d(obj, address):
    result = {'D1': unpack('>B', obj[address:address + 1])[0],
              'D2': [i for i in unpack('>HH', obj[address + 1:address + 5])],
              'D3': unpack('>L', obj[address + 5:address + 9])[0]}
    return result


s = b'5MOMQ\x00\x00\x004TL\x90b\xc3\xb0\xc5\x0b\xd3s\xa8\x90\x0cP\xe9v\xd8.\xabgj\xd2\xb8\xea\x9aI\xd4\x06)\xabj\xfcm' \
    b'\x8b0\xde\xba\x00\x13\x00\x1c\x00%\xbfb\xa7\x95\x99\xb81\x03i\x89\xc6\xbb\xe2\xd1F\xe5[' \
    b'=\x00\x03\x00\x00\x00.\xd1\x03\x1a\x04\xd34u@\xc0)\x1a]jA\xe2\xf2\x8fd>\xb5\xfd\xd4\xe5\x05e\xb9\xb2\xc43\xe5' \
    b'\xf6Uj;!\x03 '

s2 = b'5MOMQ\x00\x00\x00J\xe3+|\xc3h\x97\xfe\xcc\xf2\xee\xaem\xdf\x14\xeb' \
     b'\xb2\xec\xf1\xaf\x8c\xb4\xb8\xff\x1b\x0bP\xc1N\xb5\xf1)\xe0=\xe67' \
     b'\xa7\x14Y\x9an\xe1\x92.\xda(\x9dJ\xd3MT{\xa6\xc9#"\x00\x13\x00\x1c\x00%\x00.' \
     b'\x007?u\xb8\xc6O}\x86^\x10\xf4!\x1b\r\x8c\x83\xed\xda\x03\x00\x05\x00\x00' \
     b'\x00@\x97\x7fO\xcb\x17\x18_:\xbf\x86eSPx\x84\xb6\x85\xac\xca\xf4\xbd@' \
     b'\xf78|\xd8\x82#\xd7*\xe2\xadpAq3'

print(main(s))
print(main(s2))
