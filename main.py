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

# return the second value of the list to sort it
def sortOff(list):
    return list[1]


def sort_dict_by_value(dic):
    return dict(sorted(dic.items(), key=sortOff, reverse=True))

# print on console the report on the count of caracter
def print_report(text):
    chars_count = count_each_letters(text)
    chars_count = sort_dict_by_value(chars_count)

    print("--- Begin report of books/frankenstein.txt ---")

    print(f"{count_words(text)} words found in the document\n")

    for letter in chars_count:
        print(f"The {letter} characters was found {chars_count[letter]} times")
    
    print("--- End Report ---")

# return an int of total words
def count_words(text):
    return len(text.split())

# return in string of the entire file
def get_book_text(path):
    with open(path) as f:
        return f.read()
        


main()