from math import remainder
from letter_state import LetterState

# We are making this class wordle and throught this we are going to 
# call a instance of the this class which is going to be our actual game.
class Wordle:

    MAX_ATTEMPTS = 6 # The number of rows which is visible to us.
    WORD_LENGTH = 5 # The number of columns visible to us.
    VOIDED_LETTER = "*"

    # This is the function which will run when we will construct the class.
    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)

    def guess(self, word: str):
        word = word.upper()

        # Initialize the results array with all GREY letters.
        result = [LetterState(x) for x in word]

        # Make a copy of the secret so we can cross out 'used' letters.
        remaining_secret = list(self.secret)

        # First, check for GREEN letters.
        for i in range(self.WORD_LENGTH):
            letter = result[i]
            if letter.character == remaining_secret[i]:
                letter.is_in_position = True
                remaining_secret[i] = self.VOIDED_LETTER

        # Loop again and check for YELLOW letters.
        for i in range(self.WORD_LENGTH):
            letter = result[i]

            # Skip this letter if it is already in the right place.
            if letter.is_in_position:
                continue

            # Otherwise, check if the letter is in the word, and void that index.
            for j in range(self.WORD_LENGTH):
                if letter.character == remaining_secret[j]:
                    remaining_secret[j] = self.VOIDED_LETTER
                    letter.is_in_word = True
                    break

        return result

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    # This property checks if remaining_attempts is greater than zero and the puzzle is still not solved
    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
