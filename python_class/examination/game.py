import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.score = {"player": 0, "computer": 0}
        
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Its a tie"
        elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
            self.score["player"] += 1
            return "You win!"
        else:
            self.score["computer"] += 1
            return "Computer win!"
    
    def play_game(self):
        print("Welcome to rock, paper, scissors")
        
        while True:
            player_choice = input("Enter rock, paper, scissors (or 'quit' to quit): ").lower()
            if player_choice == "quit":
                print("Thanks for playing")
                break
            if player_choice not in self.choices:
                print("Invalid choice! Please try again")
                continue
            
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            
            result = self.determine_winner(player_choice, computer_choice)
            print(result)
            print(f"Score - Player:{self.score["player"]}, Computer:{self.score["computer"]}")
            
            if __name__ == "__main__":
                game = RockPaperScissors
                game.play_game()