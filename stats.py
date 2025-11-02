def get_book_text(file_path: str):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_words_count(book_content: str):
    words = book_content.split()
    return len(words)


