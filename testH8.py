'''import re
def main(x):
    r = r"\[\[\s*variable\s*list\(\s*([^)]*)\)\s*=>\s*([^.]*)"
    z = re.findall(r, x)
    print (z)
    ls2 = []
    for ints, key in z:
        print('key=', key)
        print('ints=', ints)
        ls = []
        for i in ints.split():
            print('i=', i)
            if i == ".":
                continue
            ls.append(int(i))
            print('ls=', ls)
        p = (key, ls)
        print('p=', p)
        ls2.append(p)
        print('ls2=', ls2)
    return ls2

print(main('\begin [[ variable list(-8983 . 6385 )=>aoren_461. ]], [[variable list( -6192 . 4321 . -1780 . 955) =>riuser_156. ]],[[ variable list(-9612 . -2556) =>eres.]], [[ variable list( -9853 . -4639 . -2997) => zaisa_42. ]], \end'))

'''
'''import re
def main(x):
    r =  r'\s*[^"]+\"да\s*::=\s*#[(][^)]+[)]'
    #r = r'"(.*?)"+\s* ::=\s*#[(][^)]+[)]'
    r0 = re.compile(r'"(.*?)"'
                    r'\"[^\"]+\"'
                    r'[-[0-9]+')
    r2 = re.compile(r'(\")?'
                    r'(\w+?)'
                    r'(::=\s*#)?'
                    r'(-?\d+)')
    r3 = r'"([^"]*)"[^(]*\(([^)]*)\)\.\s*\)\)'
    res1 = re.findall(r3, x)
    result = []
    for key, ints in res1:
        print(ints)
        print(key)
        nums =[]
        for num in ints.split(', '):
            nums.append(int(num))
        p = (key, nums)
        result.append(p)
    return result
print(main('(( define "enan_447" ::= #( -1670 , -4867 ). )) (( define"onveso" ::=#( 2201 , -4667 ). ))'))
'''

'''import re
 
def main(input_str):
    block_pattern = r'\(\(\s*define\s*[\":][^\"]+\"\s*::=\s*#[(][^)]+[)]'
    name_pattern = r'\"[^\"]+\"'
    num_pattern = r'[-[0-9]+'
    result = []
    res1 = re.findall(block_pattern, input_str)
    print(res1)
    for block in res1:
        print('block', block)
        nums = []
        for num in re.findall(num_pattern, re.findall(r'\#[(][^)]+[)]', block)[0]):
            print('num', num)
            nums.append(int(num))
        result.append((re.findall(name_pattern, block)[0][1:-1], nums))
        print('result', result)
    return result
  
print(main('((define "esat"::= #(8168,-6658 , 1666, 2775 ). ))((define"atso"::=#( -8779 , 7438 ,3791 ,8884).))'))

'''


'''
def main(text):
    num = re.compile('new[ |\n](\\w+) ?:= ?(\\w+).')
    return re.findall(num, text)
print(main('[[ new zalabi := esgete_969. ]]. [[ new geer :=teisra. ]].[[new tela:= rexeat_16. ]].[[ new erce :=lasoat. ]].'))
'''

'''pat = r'\s*<:\s*global\s*([^-]*)\s*->\s*([^\.]*)\.\s*:>'
strin = '|| <:global isri_49 -> bidi_853. :><: global onorve_644 -> isti. :> ||'
print(re.findall(pat, strin))'''

'''def main(x):
    pat = r'\s*variable\s*([^=]*)\=\s*\#([^;]*)\;\s*\\end\.'
    st = re.findall(pat, x)
    nums=[]
    for key, ints in st:
        p = (key, int(ints))
        nums.append(p)
        print(nums)
    return nums
        

print(main('\begin variable quat = #9779; \end. \begin variable riondi =#-9287;\end.'))
    
'''
'''import re
def main(x):
    pat = r'\|\|\s*option \s*array\s*\(\s*([^)]*)\s*\)\s*=>\s*q\(([^)]*)\)\.\s*\|\|\;\s*'
    res = re.findall(pat, x)
    res1 = []
    for key, init in res:
        print( key)
        print( init)
        words = []
        for w in key.split('; '):
            words.append(w)
        p = (init, words)
        res1.append(p)
    return res1
        
print(main('|| option array( erus_981 ; usxe) =>q(arxeso_423). ||; ||option array(raan; onrain_135; eden_649 ; maso_394) => q(isorre). ||;'))
'''
