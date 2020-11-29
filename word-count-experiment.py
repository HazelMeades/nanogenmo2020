import spacy
from spacy.matcher import Matcher
import random

with open("nanowrimo/combined-allfinished-nanos-nofluff.txt") as word_file:
    words = word_file.readline().split() #This splits by whitespace, if you used some other delimiter specify the delimiter here as an argument.
    
#random_number = random.randrange(1,4)
random_word = random.choice(words)

random_number = random.randint(1,4)

title = []
nlp = spacy.load("en_core_web_sm") #loading a language model
matcher5 = Matcher(nlp.vocab)

#for title_word in title:
pattern = [{'POS': 'ADJ', 'IS_PUNCT': False}]
matcher5.add("Title", None, pattern)


#print("%s\n%s\n%s\n" %(random.choice(g_5),random.choice(g_7),random.choice(g_5)))

#for words in range(random_number):
    #title.append(random_word)

#print('%s\n' %(title))
#print("%s\n%s\n%s\n" %(random.choice(g_5),random.choice(g_7),random.choice(g_5)))

#for random_number
#random_title = (random_word + ' ') * random_number
#random_title.capitalize()
#print("%s\n" %(random_title.capitalize()))
