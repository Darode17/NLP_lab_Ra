##Assignment No.02##
#Name:Radhika Santosh Darode
##Roll No:16
#Batch:B1
#Title:Assignment to implement Bag of Words and TFIDF using Gensim library.

import gensim
from gensim import corpora
from gensim.utils import simple_preprocess
text1 = ["""The Dog sat
         The Dog sat in the hat
         The Dog sat with the hat."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)

text = ["""The Dog sat
         The Dog sat in the hat
         The Dog sat with the hat."""]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')
print("\n TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])

##OUTPUT##
'''
Output for Bag of Words:
{'Dog': 0, 'The': 1, 'hat': 2, 'hat.': 3, 'in': 4, 'sat': 5, 'the': 6, 'with': 7}
Bag of Words :  [[(0, 3), (1, 3), (2, 1), (3, 1), (4, 1), (5, 3), (6, 2), (7, 1)]]

Output for TFIDF:
Dictionary : 
[['dog', 3], ['hat', 2], ['in', 1], ['sat', 3], ['the', 5], ['with', 1]]

TF-IDF Vector:
[['dog', 0.43], ['hat', 0.29], ['in', 0.14], ['sat', 0.43], ['the', 0.71], ['with', 0.14]]
'''
