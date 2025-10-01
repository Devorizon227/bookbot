def get_word_count():
    with open('./books/frankenstein.txt', 'r') as book:
        words = book.read()
        numWords = len(words.split())
        return print(f"Found {numWords} total words")

def get_char_count():
    with open('./books/frankenstein.txt', 'r') as book:
        words = book.read()
        char_dict = {}
        for character in words:
            char = character.lower()
            if char in char_dict:
                char_dict[char] = char_dict[char] + 1
            else:
                char_dict[char] = 1
    print(char_dict)
    return char_dict
        
