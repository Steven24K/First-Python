print("\nThe rules:\nRock beats Scissors\nScissors beats Paper\nPaper beats Rock\n")
game = True
score = 0
lost = 0
while game == True:
 choice = input("Chose your weapon rock, paper, scissors, SPOCK or LIZARD find out what they do: \n")
 print("is your choice\n ")
 weapons =['rock' , 'paper' , 'scissors' , 'spock' , 'lizard'] 
 import random
 x = random.randint(0, 4)
 print("The computer chose: ")
 print(weapons[x])
 if choice == "rock" and x == 0:
    print("It is a tie, rock can not beat rock\n")
 if choice == "rock" and x == 1:
     lost += 1 
     print("You lost, paper wraps rock\n")
 if choice == "rock" and x == 2:
     score += 1
     print("You won, rock crushes scissors\n")
 if choice == "rock" and x == 3:
     lost += 1
     print("You lost, spock vaporizes rock")
 if choice == "rock" and x == 4:
     score += 1
     print("You won, rock crushes lizard")
 if choice == "paper" and x == 0:
     score += 1
     print("You won, paper wraps rock\n")
 if choice == "paper" and x == 1:
    print("It is a tie, paper can not beat paper\n")
 if choice == "paper" and x == 2:
     lost += 1
     print("You lost, scissors cuts paper\n")
 if choice == "paper" and x == 3:
     score += 1
     print("You won, paper disproves spock")
 if choice == "paper" and x == 4:
     lost += 1
     print("You lost, lizard eats paper" )
 if choice == "scissors" and x == 0:
     lost += 1
     print("You lost, rock crushes scissors\n")
 if choice == "scissors" and x == 1:
     score += 1
     print("You won, scissors cut paper\n")
 if choice == "scissors" and x == 2:
    print("It is a tie, scissors can not beat scissors\n")
 if choice == "scissors" and x == 3:
     lost += 1
     print("You lost, spock smashes scissors")
 if choice == "scissors" and x == 4: 
     score += 1
     print("You won, scissors decapitates lizard")
 if choice == "spock" and x == 0:
    score += 1
    print("You won, spock vaporizes rock")
 if choice == "spock" and x == 1:
    lost += 1
    print("You lost, paper disaproves spock")
 if choice == "spock" and x == 2:
    score += 1
    print("You won, spock smashes scissors")
 if choice == "spock" and x == 3:
    print("It is a tie, spock can not beat up spock")
 if choice == "spock" and x == 4:
    lost += 1
    print("You lost, lizard poisons spock")
 if choice == "lizard" and x == 0:
     lost += 1
     print("You lost, rock crushes lizard")
 if choice == "lizard" and x == 1:
     score += 1
     print("You won, lizard lizard eats paper")
 if choice == "lizard" and x == 2:
     lost += 1
     print("You lost, scissors decapitates lizard")
 if choice == "lizard" and x == 3:
     score += 1
     print("You won, lizard poisons spock")
 if choice == "lizard" and x == 4:
     print("It is tie, lizard can not beat lizard")
 if choice == "steven":
     score += 1
     print("Excelent choice, he beats everyone. You won")
 if choice == " ":
     print("Please chose a weapon")
 print("The times you won: ")
 print(score)
 print("The times you lost: ")
 print(lost)
 print("\n\n")