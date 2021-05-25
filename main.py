import json
import logging


def handle_no_morse_code_definition(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError as error:
            logging.exception(f'No Morse code definition for character: {error}')
    return wrapper


def get_morse_code_dict():
    with open('morse_code.json', mode='r') as file:
        morse_code = json.load(file)
    return morse_code


@handle_no_morse_code_definition
def code_morse(sentence_to_code):
    morse_code = get_morse_code_dict()
    coded = ''
    list_of_word = sentence_to_code.split()
    for word in list_of_word:
        for letter in word:
            morse_letter = morse_code[letter]
            if morse_letter:
                coded += morse_letter + ' '
    return coded


@handle_no_morse_code_definition
def decode_morse(sentence_to_decode):
    morse_code = get_morse_code_dict()
    decoded = ''
    list_of_symbols = sentence_to_decode.split()
    for symbol in list_of_symbols:
        for key, value in morse_code.items():
            if symbol == value:
                decoded += key
    return decoded


def run_app():
    while True:
        action = input('Do you want to code in Morse or decode?\n').lower()
        if action == 'code':
            sentence = input('Type in Sentence to code in Morse\n').lower()
            print(code_morse(sentence))
        elif action == 'decode':
            sentence = input('Type in Sentence to code in Morse\n').lower()
            print(decode_morse(sentence))
        elif action == 'exit':
            break
        else:
            print('Invalid action.')


# TODO A lot for repeated lines in both functions - refactor into one?
# TODO think about saving morse into a .wav file
if __name__ == '__main__':
    run_app()
