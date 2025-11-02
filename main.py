import sys
from stats import print_sorted_chars_count
from stats import get_book_text, get_words_count, get_chars_count, get_sorted_chars_count

def get_file_path():
    if len(sys.argv) < 1:
        raise IndexError
    return sys.argv[1]

def main():
    try:
        file_path = get_file_path()
        
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

    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    except Exception as e:
        print(e)

main()


