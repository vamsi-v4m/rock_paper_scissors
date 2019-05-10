print(" 8< === represents scissors\n 0 === represents rock\n|=| === represents paper \n\t-...- lets play-...-")
from random import  randint
player=str(input(" Rock(r)-Paper(p)-scissor(s)? \n"))
if player=='r'or player=='p' or player=='s':
    print(player,'vs',end=" ")
choice=randint(1,3)
#print(choice)
if choice==1:
    computer='r'
    print("0")
elif choice==2:
    computer='p'
    print("|=|")
if choice==3:
    computer='s'
    print("8<")
if player==computer:
    print("\nDraw")
elif player=='r' and computer == 's':
    print("\nPlayer wins! hurrah!")
elif player=='r' and computer == 'p':
    print("\ncomputer wins!")
elif player=='s' and computer=='p':
    print("\nplayer wins! hurrah!")
elif player=='p' and computer == 'r':
    print("\nplayer wins! hurrah")
elif player=='s' and computer == 'r':
    print("\ncomputer wins!")
elif player == 'p' and computer == 's':
    print("\ncomputer wins!")

