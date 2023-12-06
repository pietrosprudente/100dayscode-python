from random import randint
from art import logo

EASY_TURNS = 10
HARD_TURNS = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too Big.")
    return turns - 1
  elif guess < answer:
    print("Too Small.")
    return turns - 1
  else:
    print(f"You got a Victory Royale The number was {answer}.")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_TURNS
  else:
    return HARD_TURNS

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Hey, the number is {answer}") 

  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} tries left to guess the number.")

    guess = int(input("Make the guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You're out of tries, top #2.")
      return
    elif guess != answer:
      print("Try again.")


game()