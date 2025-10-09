def get_word_count(text):
    numWords = len(text.split())
    return numWords

def get_char_count(text):
    charDict = {}
    for character in text:
        char = character.lower()
        if char in charDict:
            charDict[char] = charDict[char] + 1
        else:
            charDict[char] = 1
    return charDict

def sort_on(items):
    return items['num']

def sort_dict(char_count):
    sortedList = []
    for char, num in char_count.items():
        sortedList.append({'char': char, 'num': num})
    sortedList.sort(reverse=True, key = sort_on)
    return sortedList
    
    #dictionary format - {"char": "b", "num": 4868}
