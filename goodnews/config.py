import os

CONFIG_FOLDER = 'config'

def read_lines(path):
    with open(path) as file:
        return file.readlines()

negative_words = read_lines(os.path.join(CONFIG_FOLDER, 'negative_words.txt'))

