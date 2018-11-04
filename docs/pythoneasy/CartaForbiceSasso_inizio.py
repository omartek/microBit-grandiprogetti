from random import randint
from time import sleep

## carta
## _____
##|     |
##|     |
##|_____|
##
## forbici
## \  /
##  \/
##  /\
## o  o
##
## sasso
##   _
##  ( )
## (___)


carte=[[" _____ ","|     |","|     |","|_____|"],
       ["\  /"," \/ "," /\\ ","o  o"],
       ["     ","  _  "," ( ) ","(___)"]]

plA=randint(0,2)
plB=randint(0,2)
print(str(plA))
print(str(plB))

if plA==0:
    if plB==0:
        print("Patta")
    elif plB==1:
        print("Vince plB")
    else:
        print("Vince plA")

if plA==1:
    if plB==1:
        print("Patta")
    elif plB==2:
        print("Vince plB")
    else:
        print("Vince plA")

if plA==2:
    if plB==2:
        print("Patta")
    elif plB==0:
        print("Vince plB")
    else:
        print("Vince plA")
