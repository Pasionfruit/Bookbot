import sys
from stats import *

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

relative_book_path = sys.argv[1]

def get_books_text():
    with open(relative_book_path) as f:
        file_contents = f.read()
        print("----------- Word Count ----------")
        get_num_words(file_contents) 
        print("--------- Character Count -------")
        char_freq = get_char_frequency(file_contents)
        dict_to_sorted_list(char_freq)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_book_path}...")
    get_books_text()
    print("============= END ===============")

main()