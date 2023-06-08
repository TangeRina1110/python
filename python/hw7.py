#def main(input_string):
#    input_string = input_string.strip('()') # удаление скобок
#    input_list = input_string.split('.') # разбиение на отдельные строки
#    result_list = []
#    for item in input_list:
#        item = item.strip(', ') # очистка от пробелов и запятых
#        name, value = item.split('::=') # разбиение на имя и значение
#        name = name.strip('"') # удаление кавычек в имени
#        result_list.append((name, value))
#    return result_list
#print(main((define "enan_447" ::= #( -1670 , -4867 ). )) (( define"onveso" ::=#( 2201 , -4667 ). ))


def main(h:str):
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
print(main('0x6b6feea0c'))
