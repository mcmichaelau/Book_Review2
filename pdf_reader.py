from pdfminer.high_level import extract_text
import re


def pdf_to_text(file, split_length):
    text = extract_text(file)

    # create a list of characters to replace
    chars = [r"\n\n(?=[a-z])", r"\n(?=[a-z])", r"(?<=[A-Z])\n(?=[A-Z])", r"(?<=[A-Z])\n\n(?=[A-Z])", r"(-)\n\n",
             r"(-)\n"]

    # loop through each character and replace it with a space
    for char in chars:
        text = re.sub(char, " ", text)

    # append the text to the list
    text_list = text.split("\n")

    # merge each the elements of the text list into strings that are less than 4000 characters and append them to a new
    # list with newlines between each element

    split_text_list = []
    for i in range(len(text_list)):
        if i == 0:
            split_text_list.append(f'\n{text_list[i]}')
        elif len(split_text_list[-1]) + len(text_list[i]) < split_length:
            split_text_list[-1] = split_text_list[-1] + f'\n{text_list[i]}'
        else:
            split_text_list.append(f'\n{text_list[i]}')

    return split_text_list


