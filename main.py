import random


def genNum():   ## Generate random 4 digit number
    g = ""
    i = 4
    while i > 0:
        g += str(random.randint(0, 9))
        i -= 1
    return g


def checkcow(gennumber, usernumber):    ## check for cows (same element with same indexes)
    cow = 0
    i = 0
    print(usernumber)
    for _ in gennumber:
        if gennumber[i] == usernumber[i]:
            cow += 1
        i += 1
    return cow


def checkbull(gennumber, usernumber):  ## check for bulls (counting duplicates between 2 sets).
    bull = 0                           ## it's going to count any duplicate so later we have to substract
    i = 0                              ## cows from the bulls
    for x in gennumber:
        if x in usernumber:
            bull += 1
    return bull


if __name__ == "__main__":
    y = genNum()
    ## print(y)
    print("Welcome to cows and bulls game!")

    while True:
        x = input("Give me 4 digit number: ")
        if len(x) < 4:      ## Just checking if given number is a 4 digit number
            print("WRONG INPUT!")
        elif len(x) > 4:
            print("WRONG INPUT!")
        else:
            cow = checkcow(y, x)
            bull = checkbull(set(y), set(x)) - cow  ## Checking the real number of bulls
            if bull < 0:
                bull = 0
            print("Cows: " + str(cow) + " Bulls: " + str(bull))
            if cow == 4:
                print("You WIN!")
                break
