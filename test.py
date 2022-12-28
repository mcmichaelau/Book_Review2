from pdf_reader import pdf_to_text
from gpt_summarize import ada_summarize, summarize_bullet_points, davinci_further_summarize, combine_list_items

key = "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"

# open the file
file = open('Asterisk copy.pdf', 'rb')

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
print(f"type combined list:{type(combined_broad_list)}")

# print spacer
print('-------------------')

specific_summary = davinci_further_summarize(combined_broad_list, key)

print(f"length specific summary: {len(specific_summary)}")
print(f"specific summary: {specific_summary}")

# output: ["The main sentiment of the text is one of admiration for the hard work, dedication, and resilience of the protagonist and their family in overcoming life's challenges.", 'The main sentiment of the text is that the protagonist has grown and matured, learning to take responsibility for their actions and forming strong connections with family members and friends.', 'The main sentiment of the text is that the protagonist has found strength and hope in a new relationship, and has been able to move past the trauma of their past to trust in someone new.', "The text conveys a sentiment of hope and resilience, as the protagonist learns to accept life's disappointments and ultimately moves on with their life, beginning a new relationship and starting college.", "The text conveys a message of hope and love, showing how the protagonist overcame mental health struggles and found self-love, allowing them to enter into a healthy relationship and ultimately become pregnant with their partner's support.", 'The main sentiment of the text is one of fear, confusion, and appreciation for the support and understanding of family during a difficult time.', 'The main sentiment of the text is one of gratitude for the support of family and friends, and how having a car provided freedom, independence, and joy.', "The main sentiment of the text is that life's challenges can lead to unexpected growth, and that love and family can provide a source of strength and stability during times of transition.", "The text reflects the protagonist's journey from a reckless lifestyle to a mature relationship, which leads to the acceptance of his family and a successful relationship with Cindy.", 'The main sentiment of the text is one of redemption, hope, and determination in the face of adversity.', 'The text conveys a sentiment of contentment, appreciation, and nostalgia as the narrator reflects on their successful career and strong bond with their family.', 'The text reflects a positive sentiment of joy and pride in the success of Matt and anticipation for having children with Jessica who will hopefully turn out just like him.', 'The main sentiment of the text is one of hope, appreciation, joy, and gratitude for the unexpected blessings life can bring.', 'The text conveys a message of self-love and acceptance, and the support of family in the journey towards it.', 'The text conveys a message of unconditional love and support for the protagonist, demonstrating a strong bond between the family members despite difficult circumstances.', "The protagonist is struggling to find a balance between her desire for independence and her parents' protective nature, but ultimately finds support from her parents and experiences positive emotions in the end.", 'The main sentiment of the text is one of family love, appreciation, and comfort in difficult times.', "The text conveys a sentiment of joy and optimism, despite the hardships faced by the narrator's family, as the speaker is in love with Milada and they are expecting a baby together, and the family is excited to welcome the new addition.", 'The text conveys a sentiment of hope and acceptance despite the difficult circumstances of a young pregnancy, as the family comes together to support Cindy and her baby.', "The sentiment of the text is one of joy, relief, and appreciation for the family's blessings.", "Despite experiencing hardship, anxiety and disappointment during the Depression and War, the narrator's family found joy and contentment in the 1960s and 70s which was disrupted by their teenage children.", 'The main sentiment of the text is that despite difficult and unpredictable circumstances, faith and love can lead to a successful outcome.', "The sentiment of the text is that Matt and Amy's love was strong enough to make the narrator feel welcomed and accepted, and Tabitha and Bart showed each other kindness and support.", 'The sentiment of the text is one of joy, relief, and acceptance as the protagonist is welcomed and accepted into a new environment and finds love in unexpected places.', 'The text expresses the bittersweet feeling of saying goodbye to a beloved friend, while also celebrating the strong bond between Matt and his friends and his courage to remain positive and welcoming even in the face of adversity.', 'The main sentiment of the text is that the protagonist is feeling a mix of emotions, including confusion, excitement, and anxiety as he embarks on a new journey with the potential to reunite with his ex-girlfriend and start a family.', 'The text conveys a sense of warmth, loyalty, and selflessness between the narrator and their friends and family as they face the challenges of change.', "The text conveys the sentiment of acceptance of life's changes and finding solace in faith and family.", 'The main sentiment of the text is that the protagonist is struggling to balance their personal life and family expectations while navigating a complex relationship with Milada.', 'The text conveys a journey from despair to hope, as the protagonist finds a loving relationship and family with Gabriel and their child.']




