from stats import get_num_words
def get_books_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        get_num_words(file_contents) 
def main():
    get_books_text()

main()