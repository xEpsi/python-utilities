'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            Programmed by Epsi
Discord: Epsi#0001 | dsc.bio/Epsi
YouTube: https://www.youtube.com/xEpsi
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

'''

# If you know a way to make this non-case-sensitive please DM me on Discord

from time import sleep
from re import search

abc=r"abcdefghijklmnopqrstuvwxyz"

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count
  
try:  
    filename = input("Enter a filename or text: ")
    with open(filename) as f:
        text = f.read()
except:
    try:
        text=filename
        print("Your text is : {}".format(text))
    except:
        print("Fatal Error")

for char in abc:
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))

print("Restart the program to make a new one")
while True:
    sleep(1)