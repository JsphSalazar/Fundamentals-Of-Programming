print ("Hello! This program will calculate the temperature")
f = input ("What is the temperature in Fahrenheit? ")
f = float (f)
c = 5 * (f - 32)/9
print ("A temperature of", f, "degrees Fahrenheit is",c,"degrees in celsius.")
if(c >= 100):
    print ("Water boils at this temperature.")
else:
    print ("Water does not boil at this temperature.")
