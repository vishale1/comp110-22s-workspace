"""Exercise 3 - Wordle."""

_author_ = "730474696"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(search_string: str, letter_search: str) -> bool:
    """Test to see if letter is in the secret_string."""
    assert len(letter_search) == 1
    i: int = 0
    while i < len(search_string):
        if search_string[i] == letter_search:
            return True 
        i += 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Tests to see if yellow or white emoji box should be added."""
    assert len(guess_word) == len(secret_word)
    resulting_emoji: str = ""
    a: int = 0
    while len(secret_word) > a:
        if guess_word[a] == secret_word[a]:
            resulting_emoji += GREEN_BOX
        elif contains_char(secret_word, guess_word[a]) is True:
            resulting_emoji += YELLOW_BOX
        else:
            resulting_emoji += WHITE_BOX
        a += 1
    return resulting_emoji


def input_guess(expected_guess: int) -> str:
    """This function tests if guess is the correct length."""
    user_guess: str = input(f"Enter a {expected_guess} character word:")
    while len(user_guess) != expected_guess:
        user_guess: str = input(f"That wasn't {expected_guess} chars! Try again:")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 0
    won: bool = False 
    while turn != 7 and won is False:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            turn += 1
            won = True
        else:
            turn += 1
    if won is True:
        print(f"You won in {turn}/6 turns!")
    else: 
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
