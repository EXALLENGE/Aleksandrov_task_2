import random

words, maxMistakes = ['world','is','amazing','place','for','death'], 5

getRandomWord = lambda: random.choice(words)

def checkLetter(letter, word, output):
    hasHit = False
    insertedLetters = [letter for letter in output if letter != "*"]
    for letterIndex in range(len(word)):
        if letter == word[letterIndex] and letter not in insertedLetters:
            hasHit, output = True, output[:letterIndex] + letter + output[letterIndex + 1:]
    return hasHit, output


def main():
    word, mistakes = getRandomWord(), 0
    print("Guess a letter:")
    output = "*" * len(word)
    while mistakes < 5:
        letter = input()
        hasHit, output = checkLetter(letter.strip().lower(), word, output)

        mistakes += 0 if hasHit else 1
        position = "Hit!" if hasHit else "Missed, mistake {0} out of {1}.".format(mistakes, maxMistakes)
        print(position)
        print("The word: {0}".format(output))
        if not output.__contains__("*"):
            print("You won!")
            break
    if mistakes > 4:
        print("You lost!")
        

main()
