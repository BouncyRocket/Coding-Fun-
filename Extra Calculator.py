import asyncio
import random
import sys
from colored import fg
color = fg('green')


def func():
    a = str("+")
    b = str("-")
    c = str("x")
    d = str("%")
    e = str("?>(=)")
    mode = input("Mode > ")
    if mode == str(a):
        var1 = input(">>>"); var2 = input (">>>"); math = int(var1) + int(var2); print(var1 + str(" + ") + var2 + str(" = ") + str(math)); print("======================================================"); print(str(""))
    if mode ==str(b):
        var1 = input(">>>"); var2 = input (">>>"); math = int(var1) - int(var2); print(var1 + str(" - ") + var2 + str(" = ") + str(math)); print("======================================================"); print(str(""))
    if mode ==str(c):
        var1 = input(">>>"); var2 = input (">>>"); math = int(var1) * int(var2); print(var1 + str(" x ") + var2 + str(" = ") + str(math)); print("======================================================"); print(str(""))
    if mode ==str(d):
        var1 = input(">>>"); var2 = input (">>>"); math = int(var1) % int(var2); print(var1 + str(" % ") + var2 + str(" = ") + str(math)); print("======================================================"); print(str(""))
    if mode ==str(e):
        print(str(""))
        print(str(""))
        print(str(""))
        print("Secret Mode Enabled")
        print(str(""))
        print(str(""))
        print(str(""))
        model = input("Yes Or No > ")
    Yes = str("y")
    no = str("n")

    if model == str(no):
        print("")
    if model == Yes:
        while True:
            p = random.randint(999999999999999999999999999999999999999,999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
            print(color + str(p))
        
func()
