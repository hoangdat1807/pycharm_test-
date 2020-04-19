from datetime import date
today=date.today()
print (" current year:",today.year)
print("Current month:",today.month)
print("Current day :", today.day)

from datetime import time
a= time()
print("a=",a)
b= time(11, 34, 56)
print("b=", b)
c= time(hour = 11, minute= 34, second =56)
print("c=", c)
d= time(11, 34, 56, 234566)
print("d=", d)

