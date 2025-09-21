import random

def get_color(color_name):      #function to handle colors.
    colors = {
        "green": "\U0001F7E9",  # for green square icon
        "yellow": "\U0001F7E8", # for yellow square icon
        "black": "\u2B1B"       # for black square icon
    }
    return colors.get(color_name)

def evaluating(guess,ans):       # function to give feedback after every guess.
    result=['']*5                # to store green,yellow or black as feedback
    ans_chars=list(ans)          # to access each letter of random word
    for i in range(5):           # to check for correct guess
        if guess[i]==ans[i]:
            result[i]=get_color("green")
            ans_chars[i]=None     # to mark a character as already matched, so that we don't reassign t to the yellow color

    for i in range(5):           # for yellow feedback
        if result[i]=='':        # to ensure we are not over-writing the correct guess
            if guess[i] in ans_chars:
                result[i]=get_color("yellow")
                ans_chars[ans_chars.index(guess[i])] = None # to mark a character as already matched,if there is any character that are repeating ,it's not reassigned yellow color because user has typed it once.
            else:
                result[i]=get_color("black")    # for assigning wrong guesses.
    return ' '.join(result)

def game_setup():                  # function to choose random word, display game state
    with open("words.txt", "r") as f:
        words = f.read().splitlines()

    ans = random.choice(words)      # choosing random word
    chances=6

    for i in range(1,chances+1):
        print(f"This is ur {i}/{chances} turn") #display game state.
        while True:
            try:
                guess = input(f"Enter your 5-letter guess: ").strip().lower()
                if len(guess) != 5:         # ensuring input is 5 letterd word
                    raise ValueError("Word must be 5 letters long")
                if not guess.isalpha():     # ensuring word is only alphabetic
                    raise ValueError("Only alphabetic characters allowed")
                break  # if guess is valid, exit the loop
            except ValueError as ve:
                print(f"Invalid input: {ve}")
            except Exception as e:
                print(f"Something went wrong: {e}")
                break

        print(evaluating(guess,ans))        # to print feedback

        if guess==ans:
            print("Congratulation! You guessed the right word.")
    else:
        print(f"Alas! You were unable to guess the right world.The word was {ans.upper()}")

def  main():   #to print a few instructions.
    print("Welcome to WORDLE!")
    print("Guess a 5-letter word. You will get a green icon if the letter is at right position,a yellow icon if letter belongs to the word but not at right position, a black icon if character doesn't belong in the word")
    game_setup()

main()
