from stats import get_char_count

def main():
    get_book_text()
    #get_word_count()
    get_char_count()

def get_book_text():
    with open('./books/frankenstein.txt', 'r') as book:
        file_contents = book.read()
        book.close()
        return file_contents
main()