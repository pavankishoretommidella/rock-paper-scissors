import random
import sys
import time
l=['ROCK','PAPER','SCISSORS']
n=int(input("enter no.of rounds you want to play"))
mypoints=0
yourpoints=0
i=1
while i<=n:
    computerch=random.randint(0,2)
    ch=int(input("enter 1 for rock\n2 for paper\n3 for scissors\n4 to exit game"))
    if ch<=3:
        print("my choice:",l[computerch])
        print("your choice:",l[ch-1])
    if ch-1==computerch:
        print("Draw")
    elif ch==1 and computerch==1:
        print("YES!!i got a point")
        mypoints+=1
    elif ch==1 and computerch==2:
        print("OH no!you got a point")
        yourpoints+=1
    elif ch==2 and computerch==2:
        print("YES!!i got a point")
        mypoints+=1
    elif ch==2 and computerch==0:
        print("OH no!you got a point")
        yourpoints+=1
    elif ch==3 and computerch==0:
        print("YES!!i got a point")
        mypoints+=1
    elif ch==3 and computerch==2:
        print("OH no!you got a point")
        yourpoints+=1
    elif ch==4:
        print("please wait...")
        time.sleep(3)
        if mypoints>yourpoints:
            print("I won the game.Better luck next time")
        elif mypoints<yourpoints:
            print("Congrats!!This time you won")
        else:
            print("Game is Draw")



        sys.exit(0)
    else:
        print("enter valid choice")
    i=i+1
print("please wait...4")
time.sleep(3)
if mypoints>yourpoints:
    print("I won the game.Better luck next time")
elif mypoints<yourpoints:
    print("Congrats!!This time you won")
else:
    print("Game is Draw")
