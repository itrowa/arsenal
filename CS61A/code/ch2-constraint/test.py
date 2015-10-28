from constraints import *

test = connector('aabbcc')['has_val']
print(test)

aa = connector()
bb = connector()
cc = connector('celsius')

aav, bbv, ccv = [connector['has_val']() for connector in (aa, bb, cc)]

print(aav)
print(ccv)
