# read the contents of the file
import string


def read_file(path):
    with open(path) as file:
        return file.read()


# print the contents of the file
def print_contents(file):
    return print(file)


# count the number of words in the file
def count_words(file):
    return len(file.split())


# count the number of character occurrences in the file
def count_characters(file):
    character_stats = {}

    for letter in string.ascii_lowercase:
        character_stats.update({letter: file.lower().count(letter)})
    return character_stats


def main():
    file_contents = "books/frankenstein.txt"

    print(count_characters(read_file(file_contents)))


main()
