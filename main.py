def main():
    path_to_file = "books/frankenstein.txt"
    # text = get_book_text(path_to_file)
    # print(text)
    print(f"--- Begin report of {path_to_file} ---")
    count_words(path_to_file)
    print()
    count_letters(path_to_file)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(path):
    text = get_book_text(path)
    print(f"{ len(text.split()) } words found in document")


def count_letters(path):
    text = get_book_text(path)
    text = text.lower()
    letters = [text[i] for i in range(len(text))]
    dict = {}
    for i in range(len(letters)):
        letter = letters[i]
        if not letter.isalpha():
            continue
        if letter not in dict:
            dict[letter] = 0
        dict[letter] += 1
    for key, value in sorted(dict.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{key}' character was found {value} times")


main()
