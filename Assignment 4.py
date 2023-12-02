##Assignment No.04##
#Name: Radhika Santosh Darode ##Roll No: 16
#Batch: B1
#Title: Generating the n gram model using nltk from nltk import ngrams
from nltk.util import ngrams #unigram model
n = 1
sentence = 'Natural language processing (NLP) is a field of computer science, artificial intelligence concerned with the interactions between computers and human'
unigrams = ngrams(sentence.split(), n) for item in unigrams:
print(item) #bigram model n = 2
sentence = 'Natural language processing (NLP) is a field of computer science, artificial intelligence concerned with the interactions between computers and human'
unigrams = ngrams(sentence.split(), n) for item in unigrams:
print(item) #trigram model n = 3
sentence = 'Natural language processing (NLP) is a field of computer science, artificial intelligence concerned with the interactions between computers and human'
unigrams = ngrams(sentence.split(), n) for item in unigrams:
print(item)
#using text file input from nltk import ngrams
file = open("/home/exam/Desktop/NLP_LAB75/al.txt") for i in file.readlines():
cumulative = i sentences = i.split(".") counter = 0
 
for sentence in sentences:
print("For sentence", counter + 1, ", trigrams are: ") trigrams = ngrams(sentence.split(" "), 3)
for grams in trigrams: print(grams)
counter += 1 print()

####OUTPUT### '''
#####Unigram Model##### ('Natural',)
('language',)
('processing',)
('(NLP)',)
('is',)
('a',)
('field',)
('of',)
('computer',)
('science,',)
('artificial',) ('intelligence',) ('concerned',)
('with',)
('the',) ('interactions',) ('between',)
('computers',)
('and',)
('human',)


###### Bigram Model ###### ('Natural', 'language')
 
('language', 'processing') ('processing', '(NLP)')
('(NLP)', 'is')
('is', 'a')
('a', 'field')
('field', 'of')
('of', 'computer')
('computer', 'science,')
('science,', 'artificial') ('artificial', 'intelligence') ('intelligence', 'concerned') ('concerned', 'with')
('with', 'the')
('the', 'interactions') ('interactions', 'between') ('between', 'computers')
('computers', 'and')
('and', 'human')


##### Trigram Model ##### ('Natural', 'language', 'processing') ('language', 'processing', '(NLP)')
('processing', '(NLP)', 'is')
('(NLP)', 'is', 'a')
('is', 'a', 'field')
('a', 'field', 'of')
('field', 'of', 'computer')
('of', 'computer', 'science,')
('computer', 'science,', 'artificial') ('science,', 'artificial', 'intelligence') ('artificial', 'intelligence', 'concerned') ('intelligence', 'concerned', 'with') ('concerned', 'with', 'the')
('with', 'the', 'interactions')
 
('the', 'interactions', 'between') ('interactions', 'between', 'computers') ('between', 'computers', 'and')
('computers', 'and', 'human') '''
