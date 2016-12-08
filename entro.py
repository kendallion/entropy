import sys
import getopt
import os
from optparse import OptionParser


def main():
    (options, args) = get_args()
    words, numbers =\
        load_read_files(options.words_file, options.numbers_file)
    words2 = words
    word_list = load_write_file(options.output_file)
    number_of_passwords = 0

    for word1 in words.readlines():
        number_of_passwords += write_password(word_list, word1.rstrip())
        number_of_passwords += write_password(word_list, word1.title().rstrip())
        number_of_passwords += write_password(word_list, word1.upper().rstrip())

    for number in numbers.readlines():
        number_of_passwords += write_password(word_list, number.rstrip())
        words.seek(0)
        for word1 in words.readlines():
            number_of_passwords += write_password(word_list, word1.rstrip() + number.rstrip())
            number_of_passwords += write_password(word_list, word1.title().rstrip() + number.rstrip())
            number_of_passwords += write_password(word_list, word1.upper().rstrip() + number.rstrip())

    numbers.seek(0)
    words.seek(0)

    for word1 in words.readlines():
        words2.seek(0)
        for word2 in words2.readlines():
            number_of_passwords += write_password(word_list, word1.rstrip() + word2.rstrip())
            number_of_passwords += write_password(word_list, word1.title().rstrip() + word2.rstrip())
            number_of_passwords += write_password(word_list, word1.rstrip() + word2.title().rstrip())
            number_of_passwords += write_password(word_list, word1.title().rstrip() + word2.title().rstrip())
            number_of_passwords += write_password(word_list, word1.upper().rstrip() + word2.rstrip())
            number_of_passwords += write_password(word_list, word1.rstrip() + word2.upper().rstrip())
            number_of_passwords += write_password(word_list, word1.upper().rstrip() + word2.upper().rstrip())
            number_of_passwords += write_password(word_list, word1.title().rstrip() + word2.upper().rstrip())
            number_of_passwords += write_password(word_list, word1.upper().rstrip() + word2.title().rstrip())

            number_of_passwords += write_password(word_list, word1.rstrip() + "." + word2.rstrip())
            number_of_passwords += write_password(word_list, word1.rstrip() + "_" + word2.rstrip())
            number_of_passwords += write_password(word_list, word1.title().rstrip() + "." + word2.rstrip())
            number_of_passwords += write_password(word_list, word1.title().rstrip() + "_" + word2.rstrip())
            number_of_passwords += write_password(word_list, word1.rstrip() + "." + word2.title().rstrip())
            number_of_passwords += write_password(word_list, word1.rstrip() + "_" + word2.title().rstrip())
            number_of_passwords += write_password(word_list, word1.title().rstrip() + "." + word2.title().rstrip())
            number_of_passwords += write_password(word_list, word1.title().rstrip() + "_" + word2.title().rstrip())
            number_of_passwords += write_password(word_list, word1.upper().rstrip() + "." + word2.rstrip())
            number_of_passwords += write_password(word_list, word1.upper().rstrip() + "_" + word2.rstrip())
            number_of_passwords += write_password(word_list, word1.rstrip() + "." + word2.upper().rstrip())
            number_of_passwords += write_password(word_list, word1.rstrip() + "_" + word2.upper().rstrip())
            number_of_passwords += write_password(word_list, word1.title().rstrip() + "." + word2.upper().rstrip())
            number_of_passwords += write_password(word_list, word1.upper().rstrip() + "_" + word2.title().rstrip())
            number_of_passwords += write_password(word_list, word1.upper().rstrip() + "." + word2.upper().rstrip())
            number_of_passwords += write_password(word_list, word1.upper().rstrip() + "_" + word2.upper().rstrip())

    for number in numbers.readlines():
        words.seek(0)
        for word1 in words.readlines():
            words2.seek(0)
            for word2 in words2.readlines():
                number_of_passwords += write_password(word_list, word1.rstrip() + word2.rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.title().rstrip() + word2.rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.rstrip() + word2.title().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.title().rstrip() + word2.title().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.upper().rstrip() + word2.rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.rstrip() + word2.upper().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.upper().rstrip() + word2.upper().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.title().rstrip() + word2.upper().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.upper().rstrip() + word2.title().rstrip() + number.rstrip())

                number_of_passwords += write_password(word_list, word1.rstrip() + "." + word2.rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.rstrip() + "_" + word2.rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.title().rstrip() + "." + word2.rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.title().rstrip() + "_" + word2.rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.rstrip() + "." + word2.title().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.rstrip() + "_" + word2.title().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.title().rstrip() + "." + word2.title().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.title().rstrip() + "_" + word2.title().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.upper().rstrip() + "." + word2.rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.upper().rstrip() + "_" + word2.rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.rstrip() + "." + word2.upper().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.rstrip() + "_" + word2.upper().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.title().rstrip() + "." + word2.upper().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.upper().rstrip() + "_" + word2.title().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.upper().rstrip() + "." + word2.upper().rstrip() + number.rstrip())
                number_of_passwords += write_password(word_list, word1.upper().rstrip() + "_" + word2.upper().rstrip() + number.rstrip())

    print ("Generated %d passwords." % number_of_passwords)


def write_password(word_list, password):
    number_of_passwords = 0
    (options, args) = get_args()
    exclamation = options.exclamation
    min_length = options.min_length

    if password.__len__() >= min_length:
        word_list.write(password + "\n")
        number_of_passwords += 1

    if exclamation and password.__len__() >= min_length + 1:
        word_list.write(password + "!\n")
        number_of_passwords += 1
    return number_of_passwords


def load_read_files(words_file, numbers_file):
    try:
        if words_file:
            words_file = open(words_file, 'r')
        else:
            words_file = open(os.path.dirname(os.path.realpath(__file__)) + '/words.txt', 'r')
    except IOError as err:
        print("{0}".format(err))

    try:
        if numbers_file:
            numbers_file = open(numbers_file, 'r')
        else:
            numbers_file = open(os.path.dirname(os.path.realpath(__file__)) + '/numbers.txt', 'r')
    except IOError as err:
        print("{0}".format(err))

    if words_file and numbers_file: 
        return words_file, numbers_file
    else: exit()


def load_write_file(output_file):
    try:
        if output_file:
            output_file = open(output_file, 'w')
        else:
            output_file = open(os.path.dirname(os.path.realpath(__file__)) + '/wordlist.txt', 'w')
    except IOError as err:
        print("{0}".format(err))

    if output_file:
        return output_file
    else: exit()


def get_args():
    try:
        parser = OptionParser()
        parser.add_option("-w", dest="words_file",
                          help="specify words text file [default is ./words.txt]", metavar="[FILE]")
        parser.add_option("-n", dest="numbers_file",
                          help="specify numbers text file [default is ./numbers.txt]", metavar="[FILE]")
        parser.add_option("-o", dest="output_file",
                          help="specify output text file [default is ./wordlist.txt]", metavar="[FILE]")
        parser.add_option("-m", dest="min_length", type=int, default=0,
                          help="specify minimum password length [default is 0]")
        parser.add_option("-e", dest="exclamation", action="store_false", default=True,
                          help="eliminates exclamation points from passwords")
    except:
        exit()
    return parser.parse_args()

if __name__ == "__main__":
    main()
