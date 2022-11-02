#!/usr/bin/python3
"""Module Documentation"""


def text_indentation(text):
    """ Indents text based on preceding characters """
    chars = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        for c in chars:
            if c in text:
                text_split = text.split(c)
                text = str()
                for i in range(len(text_split) - 1):
                    text += f'{text_split[i].strip()}\n\n'
                text += f'{text_split[i + 1].strip()}'
        print(text)
