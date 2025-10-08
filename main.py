from stats import get_char_count
from stats import sort_dict
from stats import get_word_count

def main():
    text = get_book_text()
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_chars = sort_dict(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print((f"Found {word_count} total words"))
    print("--------- Character Count -------")
    print (sorted_chars)

def get_book_text():
    with open('./books/frankenstein.txt', 'r') as book:
        fileContents = book.read()
    return fileContents
main()