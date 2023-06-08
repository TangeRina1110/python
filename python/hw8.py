import re



#def parse_string(input_str):
#    pattern = r'"(\w+)"\s*::=#\(\s*(-?\d+)\s*,\s*(-?\d+)\s*,\s*(-?\d+)\s*,\s*(-?\d+)\s*\)\.'
#    matches = re.findall(pattern, input_str)
#    result = []
#    for match in matches:
#        name, x1, y1, x2, y2 = match
#        result.append((name, [int(x1), int(y1), int(x2), int(y2)]))
#    return result

#input_str = '((define "esat"::= #(8168,-6658 , 1666, 2775 ). ))((define"atso"::= #( -8779 , 7438 ,3791 ,8884).))'
#print(parse_string(input_str))  # [('esat', [8168, -6658, 1666, 2775]), ('atso', [-8779, 7438, 3791, 8884])]

import re
def main(input_str):
    separator = "))"
    string_list = input_str.split(separator,1)
    string1 = string_list[0]
    string2 = string_list[1]

    pattern1 = r'define\s+"(\w+)"\s*::=\s*#\(\s*(-?\d+)\s*,\s*(-?\d+)\s*,\s*(-?\d+)\s*,\s*(-?\d+)\s*\)\.'
    pattern2 = r'"(.*?)"::=\s+#\((.*?)\)'
    res1 = re.findall(pattern1, string1)
  
    res2 = re.findall(pattern2, string2)

    res_1 = [(name, [int(n) for n in nums]) for name, *nums in res1]
    res_2 = [(name, [int(n) for n in nums]) for name, *nums in res2]
    result = res_1 + res_2
    return result

print(main('((define "esat"::= #(8168,-6658 , 1666, 2775 ). ))((define"atso"::=#( -8779 , 7438 ,3791 ,8884).))' ))


