#rock paper scissors
import random
rps = ("rock","scissors","paper")
comp = random.choice(rps)

choice = input("do you choose rock(R) scissors(S) or paper(P)?")
if choice == "R":
      choice = "rock"
elif choice =="P":
      choice = "paper"
elif choice == "S":
      choice = "scissors"
else:
    print(" you did not choose corecctly. you have 3 choices only. a choice has been made for you.")
    choice = "cheese"
print ("you have chosen",choice)
print("your opponant has chosen",comp)

if choice == comp:
   print( "tis a draw")
elif choice =="scissors" and comp=="paper":
   print("scissors beats paper. you win")
elif choice =="rock" and comp=="scissors":
   print("rock beats scissors. you win")
elif choice == "paper" and comp == "rock":
   print("paper covers rock. you win")
elif choice =="rock" and comp == "paper":
   print('you lose. paper covers rock')
elif choice =="scissors" and comp == "rock":
   print("you lose. rock beats scissors")
elif choice=="paper" and Comp == "scissors":
   print ("you have lost. scissors cuts paper")
elif choice == "cheese":
   print(" you cannot win this game with cheese. next time, make a choice as required. you lose.")
   
