##Assignment No.01##
#Name:Radhika Santosh Darode
##Roll No:16
#Batch:B1
#Title:Assignment to implement Bag of Words.

import gensim
from gensim import corpora

text1 = ["""Natural language processing is a machine learning technology that gives 
        computers the ability to interpret, manipulate, and comprehend human language."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)


print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)

"""The dictionary has: 20 tokens

{'Natural': 0, 'a': 1, 'ability': 2, 'and': 3, 'comprehend': 4, 'computers': 5, 'gives': 6, 'human': 7, 'interpret,': 8, 'is': 9, 'language': 10, 'language.': 11, 'learning': 12, 'machine': 13, 'manipulate,': 14, 'processing': 15, 'technology': 16, 'that': 17, 'the': 18, 'to': 19}
Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1)]]"""
