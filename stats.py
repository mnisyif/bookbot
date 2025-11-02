def get_book_text(file_path: str):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_words_count(book_content: str):
    words = book_content.split()
    return len(words)

def get_chars_count(book_content: str):
    chars_dict:dict[str, int] = {}
    for char in book_content:
        if char.lower() not in chars_dict:
            chars_dict[char.lower()] = 1
            continue
        chars_dict[char.lower()] += 1
    return chars_dict
