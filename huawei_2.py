import  re
str=input()
regix=re.compile(r'[0-9a-zA-Z]')
no_regix=re.compile(r'[^0-9a-zA-Z]')
have=re.findall(regix, str)
no_have=re.findall(no_regix,str)
#1
have=list(set(have))
print(have)
print(no_have)
#2
def leftmove(li):
    temp=li[0]
    li.pop(0)
    li.append(temp)
    return li
for i in range(10):
    have=leftmove(have)
print(have)
#3
print(sorted(have))