from time import sleep
import os

tabScelta = int(input("Quale tabellina vuoi studiare?"))
for tempo in range(3,0,-1):
    os.system("clean")
    for cont in range(11):
        print(str(tabScelta)," x ", str(cont)," = \t", int(tabScelta*cont))
        sleep(tempo)
