import random

CHOICES = ("rock", "paper", "scissors")
def get_result(user, computer):
    if user == computer:
        return "tie"
    return "win" if (CHOICES.index(user) - CHOICES.index(computer)) % 3 == 1 else "lose"

def play_game():
    user_score = 0
    computer_score = 0

    print("\n ROCK - PAPER - SCISSORS GAME ")

    while True:
        user = input("\nChoose Rock, Paper, or Scissors: ").lower()

        if user not in CHOICES:
            print(" Invalid choice! Try again.")
            continue

        computer = random.choice(CHOICES)
        result = get_result(user, computer)

        print(f"\n You chose: {user}")
        print(f" roComputer chose: {computer}")

        if result == "win":
            print("🎉 You WIN this round!")
            user_score += 1
        elif result == "lose":
            print("You LOSE this round!")
            computer_score += 1
        else:
            print("It's a TIE!")

        print(f"\n Score → You: {user_score} | Computer: {computer_score}")

        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("\n Game Over!")
            print(f"Final Score → You: {user_score} | Computer: {computer_score}")
            break

play_game()
