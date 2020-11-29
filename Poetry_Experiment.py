# Following demo: https://medium.com/better-programming/nlp-with-python-build-a-haiku-machine-in-50-lines-of-code-6c7b6de959e3
#import nltk
#import markovify
import spacy
from spacy.matcher import Matcher
import syllapy
count = syllapy.count('additional')
import random


nlp = spacy.load("en_core_web_sm") #loading a language model
matcher2 = Matcher(nlp.vocab) #https://spacy.io/api/matcher
matcher3 = Matcher(nlp.vocab)
matcher4 = Matcher(nlp.vocab)

# POS = Part of Speech
pattern = [{'POS':  {"IN": ["NOUN", "ADP", "ADJ", "ADV"]} },
           {'POS':  {"IN": ["NOUN", "VERB"]} }]
matcher2.add("TwoWords", None, pattern)

pattern = [{'POS':  {"IN": ["NOUN", "ADP", "ADJ", "ADV"]} },
           {'IS_ASCII': True, 'IS_PUNCT': False, 'IS_SPACE': False},
           {'POS':  {"IN": ["NOUN", "VERB", "ADJ", "ADV"]} }]
matcher3.add("ThreeWords", None, pattern)

pattern = [{'POS':  {"IN": ["NOUN", "ADP", "ADJ", "ADV"]} },
           {'IS_ASCII': True, 'IS_PUNCT': False, 'IS_SPACE': False},
           {'IS_ASCII': True, 'IS_PUNCT': False, 'IS_SPACE': False},
           {'POS':  {"IN": ["NOUN", "VERB", "ADJ", "ADV"]} }]
matcher4.add("FourWords", None, pattern)


# Doc = a container for accessing linguistic annotations. 
doc = nlp(open("nanowrimo/combined-allfinished-nanos-nofluff.txt").read())

# Loads patterns?
matches2 = matcher2(doc)
matches3 = matcher3(doc)
matches4 = matcher4(doc)

g_5 = []
g_7 = []

# Span = A slice from a Doc object.
for match_id, start, end in matches2 + matches3 + matches4:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    #print('span is %s' %(span))

    # Token = a word, punctuation symbol, whitespace, etc. 
    syl_count = 0
    count = 0
    for token in span:
        count += 1
        syl_count += syllapy.count(token.text)
        #print('%d: %d %s' %(count, syl_count, token.text))
    if syl_count == 5:
        if span.text not in g_5:
            g_5.append(span.text)
    if syl_count == 7:
        if span.text not in g_7:
            g_7.append(span.text)
    #print('%d tokens %d syllables found' %(count, syl_count))

print('g_5 %d g_7 %d' %(len(g_5), len(g_7)))
print("Enter for a new haiku. ^C to quit\n")
while (True):
    print("%s\n%s\n%s" %(random.choice(g_5),random.choice(g_7),random.choice(g_5)))
    input("\n")