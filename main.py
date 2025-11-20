from stats import word_count, character_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def main():
    # 1. Check if the user provided a path argument
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # 2. Capture the path from the command line
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    # 3. Update print to show the actual file being analyzed
    print(f"Analyzing book found at {book_path}...")
    
    # 4. Pass the dynamic path to your function
    text = get_book_text(book_path)
    
    word_count_value = word_count(text)
    character_counts = character_count(text)
    
    print("----------- Word Count ----------")
    print(f"Found {word_count_value} total words")    
    print("--------- Character Count -------")
    
    chars_list = []
    for char, count in character_counts.items():
        if char.isalpha():
            chars_list.append({"char": char, "num": count})
    
    chars_list.sort(reverse=True, key=sort_on)
    
    for item in chars_list:
        print(f"{item['char']}: {item['num']}")
        
    print("============= END ===============")

main()