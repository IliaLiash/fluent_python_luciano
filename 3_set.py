print('-----SET-----')
s1 = set('aabcedefrgrgtog')
s2 = set('abfgkpeepe')
print(len(s1 & s2)) #5

s1 = ('aabcedefrgrgtog')
s2 = ('abfgkpeepe')
print(set(s1) & set(s2))
print(set(s1).intersection(s2))

print('-----SET-----')
from unicodedata import name
s1 = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}
s2 = {chr(i) for i in range(250, 256)}
print(s1)
print(s2)