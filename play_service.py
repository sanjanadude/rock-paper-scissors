from random import choice

class playService:

    def __init__(self):
        self.computerScore=0
        self.playerScore=0
        self.DEFEAT_VICTORY_ARRAY = {"rock": ["paper", "scissors"],
                                "paper": ["scissors", "rock"],
                                "scissors": ["rock", "paper"]}

    def testclass(self):
        print("hello")



    def riggedchoice(self,playerChoice, winProb=60, drawProb=20):
        modified_possible_choices = []
        modified_possible_choices += [self.DEFEAT_VICTORY_ARRAY[playerChoice][1]] * winProb
        modified_possible_choices += [playerChoice] * drawProb
        modified_possible_choices += [self.DEFEAT_VICTORY_ARRAY[playerChoice][0]] * (100 - winProb - drawProb)
        return choice(modified_possible_choices)

    def decideWinner(self, userchoice, computerChoice):
        winner = "nobody"
        if userchoice != computerChoice:
            if userchoice == "rock":
                if computerChoice == "paper":
                    winner = "computer"
                else:
                    winner = "player"
            elif userchoice == "paper":
                if computerChoice == "scissors":
                    winner = "computer"
                else:
                    winner = "player"
            else:
                if computerChoice == "rock":
                    winner = "computer"
                else:
                    winner = "player"
            if winner == "computer":

                self.computerScore+=1
            else:

                self.playerScore+=1

        return winner, self.computerScore, self.playerScore


