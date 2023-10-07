import random
import time

print("Starting game.")
options = ("catapult", "shields", "swords")
time.sleep(0.5)
print("Starting game..")
player = None
time.sleep(0.5)
print("Starting game...")
cpu = random.choice(options)
time.sleep(0.5)


while player not in options:
    player = input("Enter a choice (catapult, shields and swords): ")

print(f"Player: {player}")
print(f"CPU: {cpu}")

if player == cpu:
    print("Tie")
elif player == "catapult" and cpu == "swords":
    print("Player wins")
elif player == "swords" and cpu == "shields":
    print("Player wins")
elif player == "shields" and cpu == "catapult":
    print("Player wins")
else:
    print("Computer wins")
