def get_word_count():
    with open('./books/frankenstein.txt', 'r') as book:
        words = book.read()
        numWords = len(words.split())
        return print(f"Found {numWords} total words")