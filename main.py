from stats import get_book_text, get_words_count 

def main():
    book_content = get_book_text("./books/frankenstein.txt")
    words_count = get_words_count(book_content)
    print(f"Found {words_count} total words")

main()
