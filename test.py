from pdf_reader import pdf_to_text
from gpt_summarize import ada_summarize, summarize_bullet_points, davinci_further_summarize, combine_list_items

key = "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"

# open the file
file = open('Asterisk.pdf', 'rb')

text = pdf_to_text(file, 1900)

print(f"Text: {text}")

# print spacer
print('-------------------')

broad_summary = davinci_further_summarize(text, key)

print(f"length broad summary: {len(broad_summary)}")
print(f"broad summary: {broad_summary}")

# print spacer
print('-------------------')

combined_broad_list = combine_list_items(broad_summary, 2000)

print(f"length combined list: {len(combined_broad_list)}")
print(f"combined list:{combined_broad_list}")

# print spacer
print('-------------------')

specific_summary = davinci_further_summarize(combined_broad_list, key)

print(f"length specific summary: {len(specific_summary)}")
print(f"specific summary: {specific_summary}")




