'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            Programmed by Epsi
Discord: Epsi#0001 | dsc.bio/Epsi
YouTube: https://www.youtube.com/xEpsi
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

'''

from random import randint as rndint
from time import sleep
from re import search as research
def decorate():
    print("===================")
def decorate2():
    print("===================\n")
while True:
    try:
        rstest = int()
        inputrange = int(input("How many simulations do you want? : "))
        minrange = int(input("What do you want the minimum number to be? : "))
        maxrange = int(input("What do you want the maximum number to be? : "))
        yournumber = int(input("What number do you want to count? : "))
        printbool = str(input("Do you want to print every number? Say yes or no (no saves cpu) : "))
        yournumbercount = 0
        yes_str = r"[Yy][Ee][Ss]"
        if research(yes_str, str(printbool)):
            printboolean = True
            print("")
        else:
            printboolean = False
            print("")
        for i in range(inputrange):
            randnum = rndint(minrange, maxrange)
            if printboolean == True:
                print(randnum)
            if randnum == yournumber:
                yournumbercount = yournumbercount+1
            rstest = rstest + 1
            if rstest == inputrange:
                decorate()
                print("All tests are finished")
                decorate2()
                print("Your number (which was {}) appeared {} times out of {}.".format(yournumber, yournumbercount, inputrange))
                a_number = minrange / maxrange
                percentage = "{:.2%}".format(a_number)
                print("The odds of it appearing at least once were {}".format(percentage))
                if yournumbercount > 0:
                    a_number = minrange / maxrange / yournumbercount
                    percentage = "{:.2%}".format(a_number)
                    print("The odds of it appearing {} times were {}".format(yournumbercount, percentage))
        while True:
            answer = str(input('Run again? (y/n): '))
            if answer in ('y', 'n', 'Y', 'N'):
                break
            decorate()
            print("Invalid input.")
            decorate2()
        if answer in ('y', 'Y'):
            continue
        else:
            print("Goodbye")
            sleep(1)
            break
    except:
        decorate()
        print("\nFatal error. Please restart.\n")
        decorate2()
        continue