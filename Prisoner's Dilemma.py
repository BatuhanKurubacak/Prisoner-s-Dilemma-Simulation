import random


player1=0
player2=0
c=0
d=0


print("O represent Cooperate")
print("1 represent Defect")
print("Let's play!")

for y in range(10):
    for x in range(20):
        """
        a=int(input("Player1 enter a your choice according to information:")) MANUALLY
        b=int(input("Player2 enter a your choice according to information:"))
        """
        a=bool(random.getrandbits(1))
        b=bool(random.getrandbits(1))
        """
        a=0     ALWAYS COOPERATE vs RANDOM CASE
        b=bool(random.getrandbits(1))
    
        a=1                ALWAYS DEFECT vs RANDOM CASE
        b=bool(random.getrandbits(1))
    
        """
        "ALWAYS Cooperate VS TIT FOR TAT"
        """
        e=0
        a=1
         
        if e==0:
            b=1
            c=1
        else:
            b=0
        """
        if a==0:
            if b== 0:
                player1+=4
                player2+=4
            elif b==1:
                player1+=0
                player2+=5
        elif a==1:
            if b==1:
                player1+=2
                player2+=2
            elif b==0:
                player1+=5
                player2+=0

        print("The score : player 1 = "+str(player1)+"  player 2 ="+str(player2))

    if player1<player2:
        c=c+1
    elif player1>player2:
        d=d+1
    else:
        c=c+1
        d=d+1
    print("Total Score: Player 1 = "+str(c)+" Player 2 = "+str(d))