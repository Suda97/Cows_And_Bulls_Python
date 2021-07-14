import random


def genNum():
    g = ""
    i = 4
    while i > 0:
        g += str(random.randint(0, 9))
        i -= 1
    return g


def checkcow(gennumber, usernumber):
    cow = 0
    i = 0
    print(gennumber)
    print(usernumber)
    for _ in gennumber:
        if gennumber[i] == usernumber[i]:
            cow += 1
        i += 1
    return cow


def checkbull(gennumber, usernumber):
    bull = 0
    i = 0
    for _ in gennumber:
        j = 0
        for _ in usernumber:
            if gennumber[i] == usernumber[j]:
                bull += 1
            j += 1
        i += 1
    return bull


y = genNum()
print(y)
print("Welcome to cows and bulls game!")

while True:
    x = input("Give me 4 digit number: ")
    cow = checkcow(y, x)
    bull = checkbull(y, x)
    print("Cows: " + str(cow) + " Bulls: " + str(bull))
    if cow == 4:
        print("You WIN!")
        break
