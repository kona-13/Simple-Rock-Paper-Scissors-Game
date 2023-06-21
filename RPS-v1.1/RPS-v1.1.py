import pyfiglet
import os
import random
import winsound

#All Possible User & CPU inputs
#RPS = pyfiglet.print_figlet("Rock, Paper, Scissors!", colors='GREEN')
Rock = ["Rock", "R", "rock", "r"]
Paper = ["Paper", "P", "paper", "p"]
Scissors = ["Scissors", "S", "scissors", "s"]
ansYes = ["Yes", "Y", "yes", "y"]
ansNo = ["No", "N", "no", "n"]
cpu = ["Rock", "Paper", "Scissors"]
Quit = ["Q", "q", "X", "x"]



#The title - comment this line and import pyfiglet out if won't run - it really adds nothing to the game.
pyfiglet.print_figlet("Rock, Paper, Scissors!", colors='GREEN')
print("")
print("Made by Steven (kona-13)")
print("")
print("Possible user inputs: ")
print("Rock: ", Rock, "Paper: ", Paper, "Scissors: ", Scissors)
print("Yes: ", ansYes, "No: ", ansNo, "Quit: ", Quit)
print("")

#The game logic
def game_logic():

    cpu_input = random.choice(cpu)

    if hand_input in Rock:
        print("You picked: Rock!")
        print("CPU picked:", cpu_input)

        if cpu_input == "Rock":
            print("Tie")
            winsound.PlaySound('no.wav', winsound.SND_FILENAME)
        elif cpu_input == "Paper":
            print("You Lose :(")
            winsound.PlaySound('no.wav', winsound.SND_FILENAME)
        elif cpu_input == "Scissors":
            print("You Win!")
            winsound.PlaySound('yes.wav', winsound.SND_FILENAME)
          
    
    elif hand_input in Paper:
        print("You picked: Paper!")
        print("CPU picked:", cpu_input)

        if cpu_input == "Rock":
                print("You Win!")
                winsound.PlaySound('yes.wav', winsound.SND_FILENAME)
        elif cpu_input == "Paper":
                print("Tie")
                winsound.PlaySound('no.wav', winsound.SND_FILENAME)
        elif cpu_input == "Scissors":
                print("You Lose :(")
                winsound.PlaySound('no.wav', winsound.SND_FILENAME)

    elif hand_input in Scissors:
        print("You picked: Scissors")
        print("CPU picked:", cpu_input)

        if cpu_input == "Rock":
            print("You Lose :(")
            winsound.PlaySound('no.wav', winsound.SND_FILENAME)
        elif cpu_input == "Paper":
            print("You Win!")
            winsound.PlaySound('yes.wav', winsound.SND_FILENAME)
        elif cpu_input == "Scissors":
            print("Tie")
            winsound.PlaySound('no.wav', winsound.SND_FILENAME)

    #Quit the application
    if hand_input in Quit:
        os._exit(0)


    else:
        return False

    return True


#The Game loop
while True:
    
    hand_input = input("Pick your hand: ")

    valid_choice = game_logic()


#This part is fucked so ignoring for now.
    if not valid_choice:
        #print("Sorry, please try again!")
        continue

    playAgain = input("Play again? y/n? ")

    if playAgain.lower() != "y":
        break

#Sounds from: https://wiki.teamfortress.com/wiki/Category:Audio_cues
#Sounds used: vote no.wav and vote yes.wav