def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_count = count_words(text)
    print(count_each_letters(text))
    

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



def count_words(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()
        


main()