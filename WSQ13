def babylonian(number):
    if (number == 0):
        return 0

    guess = number
    y = 0

    while (y != guess):
        y = guess
        guess = (number/guess + guess)/2
    return guess

a = int(input("Give a number: "))

b = babylonian(a)

print("The square root by babylonian method is ",b)
