import os

def read_config_file(filename):
    this_folder = os.path.dirname(__file__)
    path = os.path.join(this_folder, 'config', filename)
    
    lines = []
    with open(path) as f:
        for line in f:
            lines.append(line.strip())
    
    return lines

negative_words = read_config_file('negative_words.txt')

