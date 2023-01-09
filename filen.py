# 1. lag en if statement som sjekker et mattestykke som inneholder pluss.
# 2. endre mattestykket til modulo.
# 3. sett resultatet inn i en variabel
# 4. lag en if statement som trekker ut et tilfeldig tall i en rekke fra 1 til 10.
# 5. sjekk at dette tallet ikke er det samme som et annet tall valgt av deg

num1 = 12
num2 = 5

sum = num1 % num2

print(sum)

if sum >= 30:
    print("Over 30")
else:
    print("Under 30")


import random
myNum = 8
randomNum = random.randint(1,10)

if randomNum != myNum:
    print(randomNum, "= jepp")
else:
    print(myNum, " Is locked")