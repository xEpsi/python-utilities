"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            Programmed by Epsi
Discord: Epsi#0001 | dsc.bio/Epsi
YouTube: https://www.youtube.com/xEpsi
GitHub: https://github.com/xEpsi
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""

#OPTIONS (replace False by True to activate) (if the option is a number, change it)
#Invert the division if the total exceeds 100%:
invert = True

#Time before closing:
closetime = 1

#Add a line including raw result (float):
rawresult = True

while True:
    try:
        num1 = int(input("First number (biggest of the two): "))
        num2 = int(input("Second number (smallest one) : "))
        num3 = num2 / num1
        num4 = int(input("Digits after comma: "))
        if num4 > 10:
            print("Above 10 digts above comma, errors will happen because of Python's operation. The limit is therefore set to 10.")
            num4 = 10
        if invert == True:
            if num3 >= 1:
                num3 = num1 / num2
        percentage = "{:.{}%}".format(num3, num4) #Calculates the percentage
        print("Result: {}".format(percentage))
        if rawresult == True:
            print("Raw result: {}".format(num3)) #The rawresult option needs to be on
    except ValueError:
        print("Error: Please enter 2 whole numbers. You can then divide the result to make up for it.") #Sometimes people just input numbers with commas and my
                                                                                                        #program isn't advanced enough in order for it to work
        
    while True:
        rep = str(input('Restart? (y/n): ')) #Program restart code (the program is inside a while True loop so it just breaks when you say n)
        if rep in ('y', 'n'):
            print("-------------------------")
            break
        print("Invalid answer.")
    if rep == 'o':
        continue
    else:
        if closetime > 0:
            print("The program will shutdown in {} seconds.".format(closetime))
            from time import sleep
            sleep(closetime)
        else:
            break
        break
