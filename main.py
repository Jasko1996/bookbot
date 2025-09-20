from stats import (
    get_book_text_lowercase,
    count_alpha_characters,
    sorted_character_list,
    print_report,
    nmb_of_characters,
    sort_on
)
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

try:
    with open(book_path, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print(f"Error: file not found: {book_path}")
    sys.exit(1)
except OSError as e:
    print(f"Error opening file: {e}")
    sys.exit(1)

book = get_book_text_lowercase(book_path)

book_total_chars = nmb_of_characters(book)

book_chars = count_alpha_characters(book)

book_sorted = sorted_character_list(book_chars)



print_report(book_path, book_total_chars, book_sorted)
