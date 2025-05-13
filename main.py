from stats import wordcount, charactercount, sortTheDictionary
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
text = ""

def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents

def main ():
    text = get_book_text(book_path)
    #print(text)
    allWords = wordcount(text)
    allChars = charactercount(text)
    sorted_report = sortTheDictionary(allChars)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {allWords} total words")
    print(f"--------- Character Count -------")
    for entry in sorted_report:
        print(f"{entry['char']}: {entry['num']}")
    print(f"============= END ===============")
    
main()
