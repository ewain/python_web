import math
from decimal import Decimal
#d = Decimal((-(2/3)*math.log((2/3), 2) -(1/3)*math.log((1/3), 2)))
#lesson26
print ("a: ", (-(2/3.0)*math.log((2/3.0), 2) -(1/3.0)*math.log((1/3.0), 2)))
a = (-(2/3.0)*math.log((2/3.0), 2) -(1/3.0)*math.log((1/3.0), 2))
print (1-3/4.0* a)

#lesson 4 information gain calculation part 9
#information gain= entropy (parent) -[weighted average]*entropy(children)

print ("lesson4 ->30: ", 1-(-(1/2.0)*math.log(1/2.0,2)-(1/2.0)*math.log(1/2.0,2)))


print ("1/2*log 1/2 : ", ((1/2.0)*math.log(1/2.0,2)))
