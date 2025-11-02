from stats import print_sorted_chars_count
from stats import get_book_text, get_words_count, get_chars_count, get_sorted_chars_count

def sort_on(items):
    return items["num"]

def main():
    file_path = "books/frankenstein.txt"

    book_content = get_book_text(file_path)
    words_count = get_words_count(book_content)

    chars_count = get_chars_count(book_content)
    sorted_chars_count = get_sorted_chars_count(chars_count) 

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    print_sorted_chars_count(sorted_chars_count)
    print("============= END ===============")

main()


