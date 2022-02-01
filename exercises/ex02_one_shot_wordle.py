"""EX02 - One Shot Worlde."""

_author_ = 730474696

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# establishing the word users will guess and taking in their input
secret_word: str = "python"
guess = str(input(f"What is your {len(secret_word)}-letter guess? "))

# testing to see if the guessed word is the same length as the secret word
while len(guess) != len(secret_word):
    guess = str = input(f"That was not {len(secret_word)} letters! Try again: ")

# creating an index counting variable and an emoji string
i: int = 0
resulting_emoji = str = ""

while i < len(secret_word):
    # if the placement and letter of the guess match the placement and letter of the secret word, a green box is added.
    if guess[i] == secret_word[i]:
        resulting_emoji += GREEN_BOX
    elif guess[i] != secret_word[i]:
        letter_exists: bool = False
        a: int = 0 
        # while loop that tests to see if letter of guess matches a letter in the secret word, even if placement does not match
        while letter_exists is not True and a < len(secret_word):
            if secret_word[a] == guess[i]:
                letter_exists = True
            else:
                a += 1
        # if loop that adds a yellow box to the string if the letter is in the secret word, but not same placement
        if letter_exists is True:
            resulting_emoji += YELLOW_BOX
        # if the letter is not found in the secret word at all, then a white box is added. 
        elif letter_exists is False:
            resulting_emoji += WHITE_BOX 
    i += 1 

print(resulting_emoji)
if guess != secret_word:
    print("Not quite. Play again soon!")
if guess == secret_word:
    print("Woo! You got it!")