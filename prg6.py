#Write a random number generator that generate random numbers between 1 and 6 (simulates a dice)
import random
def dice():
    Lst=[]
    a=random.randint(1,6)
    Lst.append(a)
    return Lst

n=1
while (n==1):
    n = int(input ("Enter 1 to roll a dice:"))
    print(dice())

    if n!=1:
        print('Game Over')
