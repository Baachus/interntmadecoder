"""Rock, Paper, Scissors game"""
from random import choice
from typing import Optional

class Game:
    """Rock, Paper, Scissors game"""
    def __init__(self) -> None:
        self._throw = None

    @property
    def throw(self) -> Optional[str]:
        """Returns the throw"""
        return self._throw

    @throw.setter
    def throw(self, throw: str) -> None:
        """Sets the throw"""
        self._throw = throw

    def random_throw(self) -> str:
        """Returns a random throw"""
        self._throw = choice(['rock', 'paper', 'scissors'])
        return self._throw or ""

    def play(self, throw: str) -> str:
        """Returns the result of the game"""
        if throw == self._throw:
            return f'I picked {self._throw}, it is a tie'
        elif throw == 'rock' and self._throw == 'scissors':
            return f'I picked {self._throw}, you win!'
        elif throw == 'paper' and self._throw == 'rock':
            return f'I picked {self._throw}, you win!'
        elif throw == 'scissors' and self._throw == 'paper':
            return f'I picked {self._throw}, you win!'
        else:
            return f'I picked {self._throw}, you lose!'

def main() -> None:
    """Main function"""
    game = Game()
    game.random_throw()
    play_again = 'y'

    while play_again.lower() == 'y' or play_again.lower() == 'yes':
        user_input = input('Enter your choice [rock, paper, scissors]: ')

        while user_input.lower() not in ['rock', 'paper', 'scissors']:
            user_input = input('Enter your choice [rock, paper, scissors]: ')

        print(game.play(user_input))

        play_again = input('Play again? [y/n]: ')


if __name__ == '__main__':
    main()
