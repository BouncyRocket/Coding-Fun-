import random
import math
e = 0
import json
while True:
    a = random.randint(0,20)
    b = random.randint(0,50)

    print(a)
    print(b)

    c = int(a) + int(b)

    d = input(">>")

    if d == str(c):
        print(str(""))
        print(str("==============================================================================================================================================================="))
        print(str(""))
        print("Correct")
        print(str(""))
        f = e + 1
        e = e + 1
        print(int(f))
        print(str(""))
        print(str("==============================================================================================================================================================="))
        print(str(""))
    if e == int("5"):
        print("Completed")
        break
