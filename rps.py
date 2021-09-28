import random
import pyfiglet

#RPS = pyfiglet.print_figlet("Rock, Paper, Scissors!", colors='GREEN')
Rock = ["Rock", "R", "rock", "r"]
Paper = ["Paper", "P", "paper", "p"]
Scissors = ["Scissors", "S", "scissors", "s"]
ansYes = ["Yes", "Y", "yes", "y"]
ansNo = ["No", "N", "no", "n"]
cpu = ["Rock", "Paper", "Scissors"]
cpu_input = random.choice(cpu)

#Rock, Paper & Scissors starts here:

while True:

    #print(RPS)
    pyfiglet.print_figlet("Rock, Paper, Scissors!", colors='GREEN')
    print("Made by Steven")
    print("Please enter your hand: ")

    Hand_Input = input(">>")


    if Hand_Input in Rock:
        print("You picked: Rock!")
        print("CPU picked: ", cpu_input)

        if cpu_input == "Rock":
            print("Tie")
        elif cpu_input == "Paper":
            print("You Lose :(")
        elif cpu_input == "Scissors":
            print("You Win!")
          
    
    elif Hand_Input in Paper:
        print("You picked: Paper!")
        print("CPU picked: ", cpu_input)

        if cpu_input == "Rock":
                print("You Win!")
        elif cpu_input == "Paper":
                print("Tie")
        elif cpu_input == "Scissors":
                print("You Lose :(")

    elif Hand_Input in Scissors:
        print("You picked: Scissors")
        print("CPU picked: ", cpu_input)

        if cpu_input == "Rock":
            print("You Lose :(")
        elif cpu_input == "Paper":
            print("You Win!")
        elif cpu_input == "Scissors":
            print("Tie")

    playAgain = input("Play again? y/n? ")

    if playAgain.lower() != "y":
        break


