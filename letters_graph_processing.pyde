import random

def draw():
    background(255, 204, 0)
    printLetters()

def setup():
    size(1300,800);
    
    global letters
    global sentences
    global excluded
    global deltas
    
    excluded = set()
    deltas = set()
    letters = {}
    
    sentences = []
    
    begin()
    mapLetters()

def begin():
    for sentence in sentences:
        splitSentence(sentence)

def splitSentence(sentence):
    words = sentence.split()
    for word in words:
        updateLetters(word)
        
def updateLetters(word):
    wordSize = len(word)
    for index in range(0, wordSize):
        letter = word[index]
        updateLetterEntry(letter, word, index)
    
def updateLetterEntry(letter, word, index):
    try:
        nextLetter = word[index+1]
        letters[letter][nextLetter] += 1
        letters[letter]["size"] += 1
    except KeyError:
        try:
            letters[letter][nextLetter] = 1
            letters[letter]["size"] += 1
        except:
            addLetterEntry(letter, nextLetter)
    except IndexError:
        letters[letter] = { "size": 1 }
        pass

def addLetterEntry(letter, nextLetter):
    letters[letter] = { "size": 1 }
    letters[letter][nextLetter] = 1
    
def printLetters():
    excluded = set()
    fill(0, 102, 153, 51);
    for letter in letters:
        coords = letters[letter]["coords"]
        printNode(letter)

def printNode(letter):
    coords = letters[letter]["coords"]
    ellipseSize = letters[letter]["size"] * 50
    
    fill(0, 102, 153, 51)
    ellipse(coords["x"], coords["y"], ellipseSize, ellipseSize)
    
    textSize(16)
    fill(0, 102, 153)
    text(letter, coords["x"] - 2, coords["y"] + 3)

def addEntryFromInput(letter):
    letters[letter] = { "size": 1 }
    addLocationToLetter(letter)

def mapLetters():
    radius = 20
    for x in range(-radius, radius+1):
        for y in range(-radius, radius+1):
            if x*x + y*y <= radius*radius:
                deltas.add((x,y))
                
    addLocationToLetters()

def addLocationToLetters():
    excluded = set()
    for letter in letters:
        addLocationToLetter(letter)

def addLocationToLetter(letter):
    coords = newCoords()
    excluded.update((coords["x"]+dx, coords["y"]+dy) for (dx,dy) in deltas)
    letters[letter]["coords"] = { "x": coords["x"], "y": coords["y"] }
       
def newCoords():
    rangeX = (480, 960)
    rangeY = (270, 540)

    x = random.randrange(*rangeX)
    y = random.randrange(*rangeY)
    if (x,y) in excluded or x > 800 or x < 50 or y > 600 or y < 50:
        return newCoords()
    return { "x": x, "y": y }

def keyPressed():
    if isinstance(key, basestring):
        try:
            letters[key]["size"] += 1
        except KeyError:
            addEntryFromInput(key)