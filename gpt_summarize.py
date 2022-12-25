import os
import openai


key = "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"


def ada_summarize(text_list, api_key):
    # define api key
    openai.api_key = api_key

    # create empty summary string
    summary = ''

    # loop through each item of the list
    for i in range(len(text_list)):

        response = openai.Completion.create(
            model="text-davinci-003",
            n=1,
            frequency_penalty=1.5,
            presence_penalty=-1.5,
            max_tokens=175,
            prompt=f"Summarize the following text in a single sentence: {text_list[i]}",
            temperature=0.5
        )

        # append the summary to the summary string
        summary = summary + response['choices'][0]['text']

    # split the summary into a list
    summary = summary.split('\n')

    # remove any empty strings from the list
    summary = [x for x in summary if x != '']

    # print(summary)

    return summary


def summarize_bullet_points(text_list, api_key):
    # define api key
    openai.api_key = api_key

    # create empty summary string
    summary = ''

    # good prompt: briefly summarize the following text

    # loop through each item of the list
    for i in range(len(text_list)):

        print(text_list[i])
        print('/////')
        if i == 0:
            # prompt = f"Identify the main points or arguments presented in the following document. For each main " \
            #          f"point, create a concise bullet point that captures the essence of the point. Ensure that the " \
            #          f"bullet points accurately reflect the content and meaning of the original document. Organize " \
            #          f"the bullet points in a logical order that follows the structure of the original document. Here " \
            #          f"is the document: {text_list[i]} "
            prompt = f"Summarize the main sentiment of the following text in a single sentence: {text_list[i]}"

        else:
            prompt = f"Summarize the main sentiment of the following text in a single sentence: {text_list[i]}"
        response = openai.Completion.create(
            model="text-davinci-003",
            max_tokens=1000,
            prompt=prompt,
            temperature=0
        )

        # append the summary to the summary string
        summary = summary + response['choices'][0]['text']
        print(response['choices'][0]['text'])
        print('-------------------')

    # split the summary into a list of bullet points
    summary = summary.split('\n')

    # print(summary)

    return summary


def combine_list_items(text_list, element_length):
    # combine the list items into bigger strings which remain below the element length
    combined_list = []

    for i in range(len(text_list)):
        if i == 0:
            combined_list.append(text_list[i])
        elif len(combined_list[-1]) + len(text_list[i]) < element_length:
            combined_list[-1] = combined_list[-1] + ' ' + text_list[i]
        else:
            combined_list.append(text_list[i])

    return combined_list


def davinci_further_summarize(text_list, api_key):
    # define api key
    openai.api_key = api_key

    # create empty summary string
    summary = ''

    # good prompt: briefly summarize the following text

    # loop through each item of the list
    for i in range(len(text_list)):

        prompt = f"Please summarize the main sentiment of the " \
                 f"following text in a single sentence: {text_list[i]} "

        # print(text_list[i])
        # print('/////')
        # if i == 0:
        #     # prompt = f"Identify the main points or arguments presented in the following document. For each main " \
        #     #          f"point, create a concise bullet point that captures the essence of the point. Ensure that the " \
        #     #          f"bullet points accurately reflect the content and meaning of the original document. Organize " \
        #     #          f"the bullet points in a logical order that follows the structure of the original document. Here " \
        #     #          f"is the document: {text_list[i]} "
        #     prompt = f"Summarize the main sentiment of the following text in a single sentence: {text_list[i]}"
        #
        # else:
        #     prompt = f"Summarize the main sentiment of the following text in a single sentence: {text_list[i]}"
        response = openai.Completion.create(
            model="text-davinci-003",
            max_tokens=1000,
            prompt=prompt,
            temperature=0.5,
            frequency_penalty=1.5,
            presence_penalty=-1.5,
            n=1
        )

        # append the summary to the summary string
        summary = summary + response['choices'][0]['text']


    # split the summary into a list of bullet points
    summary = summary.split('\n')

    # remove any empty strings from the list
    summary = [x for x in summary if x != '']

    # print(summary)

    return summary


def review(summary, title, author, api_key):

    openai.api_key = api_key

    response = openai.Completion.create(
        model="text-davinci-003",
        max_tokens=1000,
        prompt=f'Please write an up-beat, honest, and cheerful book review of a book called {title} written by {author}based on the followinf summary of the book: {summary}',
        temperature=0.5,
        frequency_penalty=1.5,
        presence_penalty=1,
        n=1
    )

    return response['choices'][0]['text']


