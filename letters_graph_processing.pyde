from position import *
from visual import *
from entry import *
from text import *

def draw():
    background(254,202,121, 0)
    printAllConnections(letters)
    printNodes(letters)    
#Currently printing connections first so ellipses overlap lines, ideally get this shit together and play with opacity/index or "just" draw line between closest ellipse points

def setup():
    size(1300,800);
    
    global sentences
    global letters
    global excluded
    global deltas

    sentences = ["hello this is a sample input"]    
    letters = {}
    excluded = set()
    deltas = set()
    
    begin()
    mapNodes(letters, deltas)

def begin():
    for sentence in sentences:
        splitSentence(sentence, letters)

#INPUT HANDLING (eventually move this to new file)
def keyPressed():
    if isinstance(key, basestring):
        try:
            letters[key]["size"] += 1
        except KeyError:
            addEntryFromInput(key, letters, excluded, deltas)