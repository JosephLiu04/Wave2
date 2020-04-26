from math import sqrt
a = float(input("Please enter a value for a:"))
b = float(input("Please enter a value for b:"))
c = float(input("Please enter a value for c:"))
NegB = b * -1
Quadratic = str((NegB - sqrt((b * b)- 4 * a * c)) / (2 * a))
Quadratic2 = str((NegB + sqrt((b * b)- 4 * a * c)) / (2 * a))
print(str("The roots are " + Quadratic + " and " + Quadratic2))
Dis = (b * b)- 4 * a * c
if Dis > 0:
    print("There are 2 real roots")
elif Dis == 0:
    print("There is 1 real root")
else:
    print("There are no real roots")