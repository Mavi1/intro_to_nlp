# === Your task ===
#	Let's have some 'fun'.
#	Go to http://en.wikipedia.org/wiki/Garden_path_sentence and have a brief read at what a 'Garden Path sentence' is (at the top) and look at the 'Examples'

#	Create the file garden.py for this task.
#	Use some Garden Path sentences or think up your own (at least 5).
#   Here, tokenise and perform Entity recognition for each of the sentences after you have stored them in a list called gardenpathSentences.
#	See how spaCy has categorised these sentences and look up the entities you dont understand
#	At the bottom of your file, write a comment about two unusual entities you found that spaCy gave one of the words of your sentences - did you expect this?

#Parsing, and Entity Recognition

#Begin Code#

import spacy

nlp = spacy.load("en_core_web_sm")

gardenpathSentences = [["The old man the boat"], ["The complex houses married and single soldiers and their families"], 
                        ["The horse raced past the barn fell"], ["The florist sent the flowers was pleased"], 
                        ["The cotton clothing is made of grows in Mississippi"], ["The sour drink from the ocean"], 
                        ["Have the students who failed the exam take the supplementary"], ["We painted the wall with cracks"]]
gardenpathSentences1 = '''"The old man the boat", "The complex houses married and single soldiers and their families",
                            "The horse raced past the barn fell", "The florist sent the flowers was pleased",
                            "The cotton clothing is made of grows in Mississippi", "The sour drink from the ocean",
                            "Have the students who failed the exam take the supplementary", "We painted the wall with cracks, 
                            "Helen is expecting tomorrow to be a bad day", "That Jill is never here hurts"'''

gardenpath_sentences_string = nlp(str(gardenpathSentences))
nlpd_gardenpath = nlp(gardenpath_sentences_string)

#print(gardenpath_sentences_string)
print(nlpd_gardenpath)

#print([each_item.orth_ for each_item in gardenpath_sentences_string if not each_item.is_punct | each_item.is_space])
#print([(each_token, each_token.label_) for each_token in gardenpath_sentences_string.ents])

print([each_item.orth_ for each_item in nlpd_gardenpath if not each_item.is_punct | each_item.is_space])
print([(each_token, each_token.label_) for each_token in nlpd_gardenpath.ents])

#The .label_ method seems to have very specific categories. That is, it categorises entities that can have only a few specific
#meanings. For example, 'Missisipi' (the US state) is classified as a geopolotical entity (GPE) and 'tomorrow' is classified as a date
#(DATE). However, I do not understand how 'a bad day', and not just 'day', is classified as a date. Furthermore, 'Helen' is classified
#as a GPE, while 'Jill' is classified as a person (Person). Additionally, when 'Jill' is added to the string, 'Helen' dissapears. That
#is, the 'Helen' object is not classified. Finally, the Entity recognition method did not categorise words like 'horse' or 'flowers'.
#I would have expected these words to be categorised as 'ANIMAL' or 'PLANT'/'VEGETATION'. Due to this, I believe that the
#'en_core_web_sm' functionality uses categories which contain entities that can only have certain meanings.