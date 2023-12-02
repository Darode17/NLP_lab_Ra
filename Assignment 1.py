##Assignment No.01##
#Name:Radhika Santosh Darode
##Roll No:16
#Batch:B1
#Title:"Text Pre-Processing using NLP operations:perform Tokenization
# Stop word removal,Lemmatization ,Part-of-Speech Tagging use any sample text"

#import Libraries
import spacy
#language model loaded
nlp = spacy.load("en_core_web_sm")
about_text = (
   "Once upon a time, there was a place called happily ever after." 
    "Though no one had ever made it there, many wrote of its wonders."
)
##1-------Tokenization---------##

about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)

##2-------Stop Words-----------###

about_doc = nlp(about_text)
print([token for token in about_doc if not token.is_stop])

##3-------Lemmatization-----------##

about_doc=nlp(about_text)
for token in about_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")

 ##4-------Part of Speech----------##   

# OUTPUT #
'''Once 0
upon 5
a 10
time 12
, 16
there 18
was 24
a 28
place 30
called 36
happily 43
ever 51
after 56
. 61
Though 62
no 69
one 72
had 76
ever 80
made 85
it 90
there 93
, 98
many 100
wrote 105
of 111
its 114
wonders 118
. 125

a
about
above
across
after
afterwards
again
against
ain't
all
                Once : once
                 was : be
              called : call
              Though : though
                 had : have
                made : make
               wrote : write
             wonders : wonder     

TOKEN: Once
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: upon
=====
TAG: IN         POS: SCONJ
EXPLANATION: conjunction, subordinating or preposition

TOKEN: a
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: time
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: there
=====
TAG: EX         POS: PRON
EXPLANATION: existential there

TOKEN: was
=====
TAG: VBD        POS: VERB
EXPLANATION: verb, past tense

TOKEN: a
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: place
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: called
=====
TAG: VBN        POS: VERB
EXPLANATION: verb, past participle

TOKEN: happily
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: ever
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: after
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: Though
=====
TAG: IN         POS: SCONJ
EXPLANATION: conjunction, subordinating or preposition

TOKEN: no
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: one
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: had
=====
TAG: VBD        POS: AUX
EXPLANATION: verb, past tense

TOKEN: ever
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: made
=====
TAG: VBN        POS: VERB
EXPLANATION: verb, past participle

TOKEN: it
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: there
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: many
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: wrote
=====
TAG: VBD        POS: VERB
EXPLANATION: verb, past tense

TOKEN: of
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: its
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: wonders
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: .
=====
TAG: .          POS: PUNCT '''
