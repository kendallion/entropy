import sys
import getopt
import os
import time
from optparse import OptionParser


def main():
    start_time = time.time()
    (options, args) = get_args()
    words, numbers, word_list = \
        load_files(options.words_file, options.numbers_file, options.output_file)
    words2 = words
    number_req = options.number_req
    global exclamation
    exclamation = options.exclamation
    global min_length
    min_length = options.min_length
    global max_length
    max_length = options.max_length
    global capital_req
    capital_req = options.capital_req

    number_of_passwords = generate_passwords(words, numbers, word_list, capital_req, number_req)

    words.close()
    numbers.close()
    word_list.close()

    run_time = time.time() - start_time

    print ("Generated {} password in {} seconds.\n{} passwords/second".format(number_of_passwords, round(run_time, 2),
                                                                              round(number_of_passwords/run_time, 0)))


def generate_passwords(words, numbers, word_list, capital_req, number_req):
    words2 = words
    number_of_passwords = 0

    if number_req == 0:
        for word1 in words.readlines():
            if capital_req == 0:
                number_of_passwords += write_password(word_list, word1.rstrip())
                number_of_passwords += write_password(word_list, word1.title().rstrip())
                number_of_passwords += write_password(word_list, word1.upper().rstrip())
                words2.seek(0)
                for word2 in words2.readlines():
                    number_of_passwords += write_password(word_list, word1.rstrip() + word2.rstrip())
                    number_of_passwords += write_password(word_list, word1.rstrip() + word2.title().rstrip())
                    number_of_passwords += write_password(word_list, word1.rstrip() + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list, word1.title().rstrip() + word2.rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.title().rstrip() + word2.title().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.title().rstrip() + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list, word1.upper().rstrip() + word2.rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.upper().rstrip() + word2.title().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.upper().rstrip() + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list, word1.rstrip() + "." + word2.rstrip())
                    number_of_passwords += write_password(word_list, word1.rstrip() + "_" + word2.rstrip())
                    number_of_passwords += write_password(word_list, word1.rstrip() + "." + word2.title().rstrip())
                    number_of_passwords += write_password(word_list, word1.rstrip() + "_" + word2.title().rstrip())
                    number_of_passwords += write_password(word_list, word1.rstrip() + "." + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list, word1.rstrip() + "_" + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list, word1.title().rstrip() + "." + word2.rstrip())
                    number_of_passwords += write_password(word_list, word1.title().rstrip() + "_" + word2.rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.title().rstrip() + "." + word2.title().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.title().rstrip() + "_" + word2.title().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.title().rstrip() + "." + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.title().rstrip() + "_" + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list, word1.upper().rstrip() + "." + word2.rstrip())
                    number_of_passwords += write_password(word_list, word1.upper().rstrip() + "_" + word2.rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.upper().rstrip() + "." + word2.title().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.upper().rstrip() + "_" + word2.title().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.upper().rstrip() + "." + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.upper().rstrip() + "_" + word2.upper().rstrip())

            elif capital_req == 1:
                number_of_passwords += write_password(word_list, word1.title().rstrip())
                number_of_passwords += write_password(word_list, word1.upper().rstrip())
                words2.seek(0)
                for word2 in words2.readlines():
                    number_of_passwords += write_password(word_list, word1.rstrip() + word2.title().rstrip())
                    number_of_passwords += write_password(word_list, word1.rstrip() + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list, word1.title().rstrip() + word2.rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.title().rstrip() + word2.title().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.title().rstrip() + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list, word1.upper().rstrip() + word2.rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.upper().rstrip() + word2.title().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.upper().rstrip() + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list, word1.rstrip() + "." + word2.title().rstrip())
                    number_of_passwords += write_password(word_list, word1.rstrip() + "_" + word2.title().rstrip())
                    number_of_passwords += write_password(word_list, word1.rstrip() + "." + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list, word1.rstrip() + "_" + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list, word1.title().rstrip() + "." + word2.rstrip())
                    number_of_passwords += write_password(word_list, word1.title().rstrip() + "_" + word2.rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.title().rstrip() + "." + word2.title().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.title().rstrip() + "_" + word2.title().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.title().rstrip() + "." + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.title().rstrip() + "_" + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list, word1.upper().rstrip() + "." + word2.rstrip())
                    number_of_passwords += write_password(word_list, word1.upper().rstrip() + "_" + word2.rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.upper().rstrip() + "." + word2.title().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.upper().rstrip() + "_" + word2.title().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.upper().rstrip() + "." + word2.upper().rstrip())
                    number_of_passwords += write_password(word_list,
                                                          word1.upper().rstrip() + "_" + word2.upper().rstrip())

            else:

                if word1.__len__() >= capital_req:
                    number_of_passwords += write_password(word_list, word1.upper().rstrip())

                words2.seek(0)
                for word2 in words2.readlines():
                    if word1.__len__() >= capital_req:
                        number_of_passwords += write_password(word_list, word1.upper().rstrip() + word2.rstrip())
                        number_of_passwords += write_password(word_list, word1.upper().rstrip() + "." + word2.rstrip())
                        number_of_passwords += write_password(word_list, word1.upper().rstrip() + "_" + word2.rstrip())

                    if word1.__len__() + 1 >= capital_req:
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + word2.title().rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "." + word2.title().rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "_" + word2.title().rstrip())

                    if 2 >= capital_req:
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + word2.title().rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "." + word2.title().rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "_" + word2.title().rstrip())

                    if word1.__len__() + word2.__len__() >= capital_req:
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + word2.upper().rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "." + word2.upper().rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "_" + word2.upper().rstrip())

                    if word2.__len__() >= capital_req:
                        number_of_passwords += write_password(word_list, word1.rstrip() + word2.upper().rstrip())
                        number_of_passwords += write_password(word_list, word1.rstrip() + "." + word2.upper().rstrip())
                        number_of_passwords += write_password(word_list, word1.rstrip() + "_" + word2.upper().rstrip())

                    if word2.__len__() + 1 >= capital_req:
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + word2.upper().rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "." + word2.upper().rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "_" + word2.upper().rstrip())

    for number in numbers.readlines():
        if number.__len__() > number_req:
            if capital_req == 0:
                number_of_passwords += write_password(word_list, number.rstrip())

            words.seek(0)
            for word1 in words.readlines():
                if capital_req == 0:
                    number_of_passwords += write_password(word_list, word1.rstrip() + number.rstrip())
                    number_of_passwords += write_password(word_list, word1.title().rstrip() + number.rstrip())
                    number_of_passwords += write_password(word_list, word1.upper().rstrip() + number.rstrip())
                    words2.seek(0)
                    for word2 in words2.readlines():
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + "." + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + "_" + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + "." + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + "_" + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + "." + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + "_" + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "." + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "_" + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "." + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "_" + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "." + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "_" + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "." + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "_" + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "." + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "_" + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "." + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "_" + word2.upper().rstrip() + number.rstrip())

                elif capital_req == 1:
                    number_of_passwords += write_password(word_list, word1.title().rstrip() + number.rstrip())
                    number_of_passwords += write_password(word_list, word1.upper().rstrip() + number.rstrip())
                    words2.seek(0)
                    for word2 in words2.readlines():
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + "." + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + "_" + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + "." + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.rstrip() + "_" + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "." + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "_" + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "." + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "_" + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "." + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.title().rstrip() + "_" + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "." + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "_" + word2.rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "." + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "_" + word2.title().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "." + word2.upper().rstrip() + number.rstrip())
                        number_of_passwords += write_password(word_list,
                                                              word1.upper().rstrip() + "_" + word2.upper().rstrip() + number.rstrip())

                else:

                    if word1.__len__() >= capital_req:
                        number_of_passwords += write_password(word_list, word1.upper().rstrip() + number.rstrip())

                    words2.seek(0)
                    for word2 in words2.readlines():
                        if word1.__len__() >= capital_req:
                            number_of_passwords += write_password(word_list,
                                                                  word1.upper().rstrip() + word2.rstrip() + number.rstrip())
                            number_of_passwords += write_password(word_list,
                                                                  word1.upper().rstrip() + "." + word2.rstrip() + number.rstrip())
                            number_of_passwords += write_password(word_list,
                                                                  word1.upper().rstrip() + "_" + word2.rstrip() + number.rstrip())

                        if word1.__len__() + 1 >= capital_req:
                            number_of_passwords += write_password(word_list,
                                                                  word1.upper().rstrip() + word2.title().rstrip() + number.rstrip())
                            number_of_passwords += write_password(word_list,
                                                                  word1.upper().rstrip() + "." + word2.title().rstrip() + number.rstrip())
                            number_of_passwords += write_password(word_list,
                                                                  word1.upper().rstrip() + "_" + word2.title().rstrip() + number.rstrip())

                        if 2 >= capital_req:
                            number_of_passwords += write_password(word_list,
                                                                  word1.title().rstrip() + word2.title().rstrip() + number.rstrip())
                            number_of_passwords += write_password(word_list,
                                                                  word1.title().rstrip() + "." + word2.title().rstrip() + number.rstrip())
                            number_of_passwords += write_password(word_list,
                                                                  word1.title().rstrip() + "_" + word2.title().rstrip() + number.rstrip())

                        if word1.__len__() + word2.__len__() >= capital_req:
                            number_of_passwords += write_password(word_list,
                                                                  word1.upper().rstrip() + word2.upper().rstrip() + number.rstrip())
                            number_of_passwords += write_password(word_list,
                                                                  word1.upper().rstrip() + "." + word2.upper().rstrip() + number.rstrip())
                            number_of_passwords += write_password(word_list,
                                                                  word1.upper().rstrip() + "_" + word2.upper().rstrip() + number.rstrip())

                        if word2.__len__() >= capital_req:
                            number_of_passwords += write_password(word_list,
                                                                  word1.rstrip() + word2.upper().rstrip() + number.rstrip())
                            number_of_passwords += write_password(word_list,
                                                                  word1.rstrip() + "." + word2.upper().rstrip() + number.rstrip())
                            number_of_passwords += write_password(word_list,
                                                                  word1.rstrip() + "_" + word2.upper().rstrip() + number.rstrip())

                        if word2.__len__() + 1 >= capital_req:
                            number_of_passwords += write_password(word_list,
                                                                  word1.title().rstrip() + word2.upper().rstrip() + number.rstrip())
                            number_of_passwords += write_password(word_list,
                                                                  word1.title().rstrip() + "." + word2.upper().rstrip() + number.rstrip())
                            number_of_passwords += write_password(word_list,
                                                                  word1.title().rstrip() + "_" + word2.upper().rstrip() + number.rstrip())

    numbers.seek(0)
    words.seek(0)

    for number in numbers.readlines():
        if number.__len__() >= number_req:
            words.seek(0)

    return number_of_passwords


def write_password(word_list, password):
    number_of_passwords = 0

    if min_length <= password.__len__() <= max_length:
        word_list.write(password + "\n")
        number_of_passwords += 1

    if exclamation and min_length + 1 <= password.__len__() <= max_length - 1:
        word_list.write(password + "!\n")
        number_of_passwords += 1
    return number_of_passwords


def load_files(words_file, numbers_file, output_file):
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

    try:
        if output_file:
            output_file = open(output_file, 'w')
        else:
            output_file = open(os.path.dirname(os.path.realpath(__file__)) + '/wordlist.txt', 'w')
    except IOError as err:
        print("{0}".format(err))

    if words_file and numbers_file and output_file:
        return words_file, numbers_file, output_file
    else:
        exit()


def get_args():
    parser = OptionParser()
    parser.add_option("-w", dest="words_file", metavar="[FILE]",
                      help="specify words text file [default is ./words.txt]")
    parser.add_option("-n", dest="numbers_file", metavar="[FILE]",
                      help="specify numbers text file [default is ./numbers.txt]")
    parser.add_option("-o", dest="output_file", metavar="[FILE]",
                      help="specify output text file [default is ./wordlist.txt]")
    parser.add_option("-m", dest="min_length", type=int, default=0, metavar="[INTEGER]",
                      help="specify minimum password length [default is 0]")
    parser.add_option("-x", dest="max_length", type=int, default=64, metavar="[INTEGER]",
                      help="specify maximum password length [default is 64]")
    parser.add_option("-c", dest="capital_req", type=int, default=0, metavar="[INTEGER]",
                      help="specify how many capital letters are required [default is 0]")
    parser.add_option("-b", dest="number_req", type=int, default=0, metavar="[INTEGER]",
                      help="specify how many numbers are required [default is 0]")
    parser.add_option("-e", dest="exclamation", action="store_false", default=True,
                      help="turns off appending of exclamation points")
    return parser.parse_args()

if __name__ == "__main__":
    main()
