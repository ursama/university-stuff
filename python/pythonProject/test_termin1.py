from termin1 import Segregator

s1 = Segregator(maxKartek=400, ileStron=30)
s2 = Segregator(maxKartek=300, ileStron=21)

s3 = s1 + s2
print(s3)

if s1 > s2:
    print(s1)
else:
    print(s2)

s1.ile += s2.ile
print(s1)
s2.oproznij()
print(s2)

del s2.ile
print(s2)
