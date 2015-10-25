def palindrome(x):
    x = str(x)
    x = x[::-1]
    x = int(x)
    return x

print("Calculating whether each value is one of: palidrome, non-lychrel or lychre candidate")

numbers = []
lychrel = []

x = int(input("Give the lower bound of numbers to consider: "))
h = int(input("Give the upper bound of numbers to consider: "))

print ("The results are for the range",x,"to",h)
for i in range(h - x+1):
    numbers.append(x)
    x = x+1
s = 0
t = 0
st = 0
for i in numbers:
    y = palindrome(i)
    if (i == y):
        s = s + 1
    else:
        z = i + y
        y1 = palindrome(z)
        for i1 in range(30):
            if (z == y1):
                st = st+1
                break
            else:
                z = z + y1
                y1 = palindrome(z)
                if (i1 == 29):
                    t = t+1
                    lychrel.append(i)

print("Natural palindromes:",s)
print("Non-lychrel (become palindrome):",st)
print("Lychrel candidates:",t)
if t!= 0:
    print ("Found lychrel number:",lychrel)
