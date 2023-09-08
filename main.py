import random
import time
while True:
    choices = ["rock", "paper", "scissors"]

    enemy = random.choice(choices)
    player = None
    for seconds in range(3, 0, -1):
        print(seconds)
        time.sleep(1)  # 1-second sleep
    while player not in choices:
        player = input("rock paper or scissors? : ").lower()

    if player == enemy:
        print("You: " + player)
        print("Computer: " + enemy)
        print("Tie!")

    elif player == "rock":
        if enemy == "paper":
            print("You: " + player)
            print("Computer: " + enemy)
            print("You lose!")
        if enemy == "scissors":
            print("You: " + player)
            print("Computer: " + enemy)
            print("You win!")
    elif player == "scissors":
        if enemy == "rock":
            print("You: " + player)
            print("Computer: " + enemy)
            print("You lose!")
        if enemy == "paper":
            print("You: " + player)
            print("Computer: " + enemy)
            print("You win!")
    elif player == "paper":
        if enemy == "scissors":
            print("You: " + player)
            print("Computer: " + enemy)
            print("You lose!")
        if enemy == "rock":
            print("You: " + player)
            print("Computer: " + enemy)
            print("You win!")

    play_again =input("Play again?(y/n): ").lower()
    if play_again != "y":
        break

print("Bye...")