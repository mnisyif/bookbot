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

def sort_on(items):
    return items["num"]

def get_sorted_chars_count(chars_count: dict):
    list_chars_count = []

    for item in chars_count:
        new_dict = {"char": item, "num": chars_count[item]}
        list_chars_count.append(new_dict)
    
    list_chars_count.sort(reverse=True, key=sort_on)
    return list_chars_count

def print_sorted_chars_count(chars_count: list):
    for item in chars_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
