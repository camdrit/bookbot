import sys

from stats import count_words
from stats import count_char_occurances
from stats import make_report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")

    path = sys.argv[1]
    book_text = get_book_text(path)
    print(f"Analyzing book found at {path}")

    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_stats = make_report(count_char_occurances(book_text))
    for stat in char_stats:
        if stat["char"].isalpha():
            print(f"{stat["char"]}: {stat["num"]}")
    
    print("============= END ===============")

main()