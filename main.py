def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text)
    

# return a dictionary of the count of all caracters in the text
def count_each_letters(text):
    text = text.lower()
    letters = dict()
    for c in text:
        if (not c.isalpha()):
            continue

        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1
    
    return letters

# print on console the report on the count of caracter
def print_report(text):
    chars = count_each_letters(text)
    chars = dict(sorted(chars.items()))

    print("--- Begin report of books/frankenstein.txt ---")

    print(f"{count_words(text)} words found in the document\n")

    for letter in chars:
        print(f"The {letter} characters was found {chars[letter]} times")
    
    print("--- End Report ---")

# return an int of total words
def count_words(text):
    return len(text.split())

# return in string of the entire file
def get_book_text(path):
    with open(path) as f:
        return f.read()
        


main()