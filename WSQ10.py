import math

a = float(input("Type the first number: "))
b = float(input("Type the second number: "))
c = float(input("Type the tirth number: "))
d = float(input("Type the fourth number: "))
e = float(input("Type the fifth number: "))
f = float(input("Type the sixth number: "))
g = float(input("Type the seventh number: "))
h = float(input("Type the eighth number: "))
i = float(input("Type the nineth number: "))
j = float(input("Type the tenth number: "))

list = [a,b,c,d,e,f,g,h,i,j]
print(list)

average = sum(list) / len(list)
print(average)

squares = (list[0]**2 + list[1]**2 + list[2]**2 + list[3]**2 + list[4]**2 + list[5]**2 + list[6]**2 + list[7]**2 + list[8]**2 + list[9]**2)/10
ec = (squares-average**2)**(1/2)
print(ec)
