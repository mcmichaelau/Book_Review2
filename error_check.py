from pdf_reader import pdf_to_text
from gingerit.gingerit import GingerIt
import pdfquery
from better_profanity import profanity
import time
import language_tool_python


def collect_errors(file):

    tool = language_tool_python.LanguageToolPublicAPI('en-US')

    # define the pdf
    pdf = pdfquery.PDFQuery(file)

    # load the pdf
    pdf.load()

    # define the text string
    text = ''

    error_list = []

    mature_list = []

    # loop through each page of the pdf
    for i in range(1, pdf.doc.catalog['Pages'].resolve()['Count'] + 1):

        # define the page
        page = pdf.pq(f'LTPage[pageid="{i}"]')

        print(f'Page {i}')

        #   # define the text
        page_text = page.text()

        for sentence in page_text.split('.'):
            # replace line breaks with a space
            sentence = sentence.replace('\n', ' ')

            # check for mature content
            mature = profanity.contains_profanity(sentence)

            if mature:
                mature_list.append(f'Page{i}:{sentence}')

            try:
                matches = tool.check(sentence)

            except:
                time.sleep(600)
                matches = tool.check(sentence)

            if matches is None:
                pass

            else:
                for match in matches:
                    error_list.append(f"Page {i}: {match.context} --> {match.replacements}")
                # error_list.append(matches)

    tool.close()

    return error_list, mature_list


def sort_mature(mature_list, filename):
    for item in mature_list:
        print(item)
        print('Keep? (y/n)')
        # create text input
        keep = input()
        if keep == 'y':
            # append error to text file
            with open(f'{filename}_mature.txt', 'a') as f:
                f.write(f"{item}\n")
        elif keep == 'n':
            pass


def sort_errors(error_list, filename):
    for error in error_list:
        print(error)
        print('Keep? (y/n)')
        # create text input
        keep = input()
        if keep == 'y':
            # append error to text file
            with open(f'{filename}_errors.txt', 'a') as f:
                f.write(f"{error}\n")
        elif keep == 'n':
            pass
