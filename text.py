from entry import updateLetterEntry

def splitSentence(sentence, letters):
    words = sentence.split()
    for word in words:
        updateLetters(word, letters)

def updateLetters(word, letters):
    wordSize = len(word)
    for index in range(0, wordSize):
        letter = word[index]
        updateLetterEntry(letter, word, index, letters)
        