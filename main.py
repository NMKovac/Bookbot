def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


from stats import num_words

def main():
    path = "/Users/nathankovac/python Learning/Bookbot/books/frankenstien.txt"
    file_contents = get_book_text(path)
    amount = num_words(file_contents)
    return print(f"{amount} words in the text")


main()



