from position import addLocationToNode

def addLetterEntry(letter, nextLetter, letters):
    letters[letter] = { "size": 1 }
    letters[letter][nextLetter] = 1

def addEntryFromInput(letter, nodes, excluded, deltas):
    nodes[letter] = { "size": 1 }
    addLocationToNode(nodes[letter], excluded, deltas)

def updateLetterEntry(letter, word, index, letters):
    try:
        nextLetter = word[index+1]
        letters[letter][nextLetter] += 1
        letters[letter]["size"] += 1
    except KeyError:
        try:
            letters[letter][nextLetter] = 1
            letters[letter]["size"] += 1
        except:
            addLetterEntry(letter, nextLetter, letters)
    except IndexError:
        letters[letter] = { "size": 1 }