from stats import get_num_words, get_character_count, sorting
import sys
def main():
    if(len(sys.argv)<2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print('============ BOOKBOT ============')
    print(f"Analyzing book found at books/frankenstein.txt...")
    get_num_words(sys.argv[1])
    sorting(sys.argv[1])
    get_character_count(sys.argv[1])
    print('============= END ===============')



main()