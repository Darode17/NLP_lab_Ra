##Assignment No.06##
#Name: Radhika Santosh Darode ##Roll No: 16
#Batch: B1
#Title: Assignment Based on Dependancy import spacy
nlp = spacy.load("en_core_web_sm")
piano_text = "Push back the result of the evaluation. Repeat it till the end of the expression.Checkout examples that are mention below in table "
piano_doc = nlp(piano_text) for token in piano_doc:
print( f""" TOKEN: {token.text}
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
) """
OUTPUT: TOKEN: Push token.tag_ = 'VB'
token.head.text = 'Push' token.dep_ = 'ROOT'

TOKEN: back token.tag_ = 'RB' token.head.text = 'Push' token.dep_ = 'advmod'

TOKEN: the token.tag_ = 'DT'
token.head.text = 'result' token.dep_ = 'det'

TOKEN: result
 
token.tag_ = 'NN' token.head.text = 'Push' token.dep_ = 'dobj'

TOKEN: of
token.tag_ = 'IN' token.head.text = 'result' token.dep_ = 'prep'

TOKEN: the token.tag_ = 'DT'
token.head.text = 'evaluation' token.dep_ = 'det'

TOKEN: evaluation token.tag_ = 'NN' token.head.text = 'of' token.dep_ = 'pobj'

TOKEN: .
token.tag_ = '.' token.head.text = 'Push' token.dep_ = 'punct'

TOKEN: Repeat token.tag_ = 'VB' token.head.text = 'Repeat' token.dep_ = 'ROOT'

TOKEN: it
token.tag_ = 'PRP' token.head.text = 'Repeat' token.dep_ = 'dobj'
 
TOKEN: till token.tag_ = 'IN'
token.head.text = 'Repeat' token.dep_ = 'prep'

TOKEN: the token.tag_ = 'DT' token.head.text = 'end' token.dep_ = 'det'

TOKEN: end token.tag_ = 'NN' token.head.text = 'till' token.dep_ = 'pobj'

TOKEN: of
token.tag_ = 'IN' token.head.text = 'end' token.dep_ = 'prep'

TOKEN: the token.tag_ = 'DT'
token.head.text = 'expression' token.dep_ = 'det'

TOKEN: expression token.tag_ = 'NN' token.head.text = 'of' token.dep_ = 'pobj'

TOKEN: .
token.tag_ = '.' token.head.text = 'Repeat' token.dep_ = 'punct'
 
TOKEN: Checkout token.tag_ = 'NN' token.head.text = 'examples' token.dep_ = 'compound'

TOKEN: examples token.tag_ = 'NNS' token.head.text = 'examples' token.dep_ = 'ROOT'

TOKEN: that token.tag_ = 'WDT'
token.head.text = 'mention' token.dep_ = 'nsubjpass'

TOKEN: are token.tag_ = 'VBP'
token.head.text = 'mention' token.dep_ = 'aux'

TOKEN: mention token.tag_ = 'NN' token.head.text = 'examples' token.dep_ = 'relcl'

TOKEN: below token.tag_ = 'RB'
token.head.text = 'mention' token.dep_ = 'advmod'

TOKEN: in
token.tag_ = 'IN' token.head.text = 'mention'
 
token.dep_ = 'prep'


TOKEN: table token.tag_ = 'NN' token.head.text = 'in' token.dep_ = 'pobj' """
