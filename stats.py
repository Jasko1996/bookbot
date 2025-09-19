def get_book_text_lowercase(file_path):
    with open(file_path, 'r') as file:
        return file.read().lower()

def nmb_of_characters(file):
    return len(file.split())

def count_alpha_characters(text):
    char_counts = {}
    for char in text:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_on(items):
    return items["num"]

def sorted_character_list(dict):
    characters_listed = []
    for key, value in dict.items():
        characters_listed.append({"char": key, "num": value})
    characters_listed.sort(reverse=True, key=sort_on)
    return characters_listed



def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for chars in chars_sorted_list:
        print(f"{chars["char"]}: {chars["num"]}")
    print("============= END ===============")

   