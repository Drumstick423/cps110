# pylint: disable=E1135,E1136

from flask import Flask, request
import random
import traceback

app = Flask(__name__)

def pickSecretNumber():
    """Returns random number between 1 and 10"""    
    return random.randrange(1, 11)

def checkGuess(guess, secretNum):
    """Prints a hint showing relation of `guess` to `secretNum`"""    
    if guess < secretNum:
        return "Your guess is too low."
    elif guess > secretNum:
        return "Your guess is too high."
    else:
        return "You got it!!"
    

@app.route("/")
def main():
    global secret
    secret = pickSecretNumber()
    return GUESS_PAGE.format('')

@app.route("/guess")
def guess():
    try:
        theGuess = int(request.args['guess'])
        result = checkGuess(theGuess, secret)
    except ValueError:
        traceback.print_exc()
        return GUESS_PAGE.format("Please enter a valid number")
    except Exception as e:
        traceback.print_exc()
        return GUESS_PAGE.format("Oops! Something weird happened. Please contact the webmaster for help.")

    if theGuess == secret:
        return """You got it!"""
    else:
        return GUESS_PAGE.format(result)
    
# Read guess page from file
with open('guessform.html','r') as f:
    GUESS_PAGE = f.read()


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
    
