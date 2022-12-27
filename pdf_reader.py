import re
import pdfquery


def pdf_to_text(file, split_length):
    # define the pdf
    pdf = pdfquery.PDFQuery(file)

    # load the pdf
    pdf.load()

    # define the text string
    text = ''

    # loop through each page of the pdf
    for i in range(1, pdf.doc.catalog['Pages'].resolve()['Count'] + 1):
        # define the page
        page = pdf.pq(f'LTPage[pageid="{i}"]')

        # define the text
        page_text = page.text()

        # append the text to the text string
        text = text + page_text + ' '

    # replace line breaks with no periods with a period and a space
    text = re.sub(r"(?<=[a-z])\n(?=[A-Z])", ". ", text)

    # create a list of characters to replace
    chars = [r"\x0c", r"\t", r"\n\n(?=[a-z])", r"\n(?=[a-z])", r"(?<=[A-Z])\n(?=[A-Z])", r"(?<=[A-Z])\n\n(?=[A-Z])",
             r"(-)\n\n",
             r"(-)\n", r"  "]

    # loop through each character and replace it with a space
    for char in chars:
        text = re.sub(char, " ", text)

    # split the text into a list of strings
    text_list = text.split("\n")

    # merge each the elements of the text list into strings that are less than 4000 characters and append them to a new
    # list with newlines between each element
    split_text_list = []
    for i in range(len(text_list)):
        if i == 0:
            split_text_list.append(f'{text_list[i]}')
        elif len(split_text_list[-1]) + len(text_list[i]) < split_length:
            split_text_list[-1] = split_text_list[-1] + f' {text_list[i]}'
        else:
            split_text_list.append(f' {text_list[i]}')

# tex

    for i in range(len(split_text_list)):
        # print(repr(split_text_list[i]))
        # replace each string with a string of the same length that does not contain \n
        # strings to replace:
        strings = ["\n", "\n ", " \n", "      ", "       ", "      ", "     ", "    ", "   ", "  "]
        for string in strings:
            split_text_list[i] = split_text_list[i].replace(string, " ")

    return split_text_list
