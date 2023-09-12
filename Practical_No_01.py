# Assignment No : 01 
# Name : Kishor Arjun More
# Roll No : 39 (B2)
# Title : "Text pre-processing using NLP operations like tokenization,stop-word removal,Lemmatization,Part-of-Speech Tagging "


#import libraries
import spacy

#language model loaded
nlp = spacy.load("en_core_web_sm")

#input
ip_text = (
    "The Group of Twenty (G20) is the premier forum for international economic cooperation."
    "It plays an important role in shaping and strengthening global architecture and governance "
    "on all major international economic issues. "
    "India holds the Presidency of the G20 from 1 December 2022 to 30 November 2023."
    )
ab_doc = nlp(ip_text)
    
#Tokenization : using idx
print("\n Tokenization\n")
for token in ab_doc:
  print (token, token.idx)
  
  
#Stop Word Removal : using is_stop 
print("\n Stop Word Removal\n")
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)
print([token for token in ab_doc if not token.is_stop])


#Lemmatization : using .lemma_
print("\n Lemmatization\n")
for token in ab_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")


#Part-of-Speech : using .pos_
print("\n Part-of-Speech\n")
for token in ab_doc:
    print(
        f"""
            TOKEN: {str(token)}
            =============================================================
            TAG: {str(token.tag_):10} POS: {token.pos_}
            EXPLANATION: {spacy.explain(token.tag_)}"""
        )



#---------------------------------------------------------------------------------------------
#OUTPUT :

# Tokenization

# The 0
# Group 4
# of 10
# Twenty 13
# ( 20
# G20 21
# ) 24
# is 26
# the 29
# premier 33
# forum 41
# for 47
# international 51
# economic 65
# cooperation 74
# . 85
# It 86
# plays 89
# an 95
# important 98
# role 108
# in 113
# shaping 116
# and 124
# strengthening 128
# global 142
# architecture 149
# and 162
# governance 166
# on 177
# all 180
# major 184
# international 190
# economic 204
# issues 213
# . 219
# India 221
# holds 227
# the 233
# Presidency 237
# of 248
# the 251
# G20 255
# from 259
# 1 264
# December 266
# 2022 275
# to 280
# 30 283
# November 286
# 2023 295
# . 299

#  Stop Word Removal

# [Group, (, G20, ), premier, forum, international, economic, cooperation, ., plays, important, role, shaping, strengthening, global, architecture, governance, major, international, economic, issues, ., India, holds, Presidency, G20, 1, December, 2022, 30, November, 2023, .]

#  Lemmatization

#                  The : the
#                   is : be
#                   It : it
#                plays : play
#              shaping : shape
#        strengthening : strengthen
#               issues : issue
#                holds : hold

#  Part-of-Speech


#             TOKEN: The
#             =============================================================
#             TAG: DT         POS: DET
#             EXPLANATION: determiner

#             TOKEN: Group
#             =============================================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: of
#             =============================================================
#             TAG: IN         POS: ADP
#             EXPLANATION: conjunction, subordinating or preposition

#             TOKEN: Twenty
#             =============================================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: (
#             =============================================================
#             TAG: -LRB-      POS: PUNCT
#             EXPLANATION: left round bracket

#             TOKEN: G20
#             =============================================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: )
#             =============================================================
#             TAG: -RRB-      POS: PUNCT
#             EXPLANATION: right round bracket

#             TOKEN: is
#             =============================================================
#             TAG: VBZ        POS: AUX
#             EXPLANATION: verb, 3rd person singular present

#             TOKEN: the
#             =============================================================
#             TAG: DT         POS: DET
#             EXPLANATION: determiner

#             TOKEN: premier
#             =============================================================
#             TAG: NN         POS: NOUN
#             EXPLANATION: noun, singular or mass

#             TOKEN: forum
#             =============================================================
#             TAG: NN         POS: NOUN
#             EXPLANATION: noun, singular or mass

#             TOKEN: for
#             =============================================================
#             TAG: IN         POS: ADP
#             EXPLANATION: conjunction, subordinating or preposition

#             TOKEN: international
#             =============================================================
#             TAG: JJ         POS: ADJ
#             EXPLANATION: adjective (English), other noun-modifier (Chinese)

#             TOKEN: economic
#             =============================================================
#             TAG: JJ         POS: ADJ
#             EXPLANATION: adjective (English), other noun-modifier (Chinese)

#             TOKEN: cooperation
#             =============================================================
#             TAG: NN         POS: NOUN
#             EXPLANATION: noun, singular or mass

#             TOKEN: .
#             =============================================================
#             TAG: .          POS: PUNCT
#             EXPLANATION: punctuation mark, sentence closer

#             TOKEN: It
#             =============================================================
#             TAG: PRP        POS: PRON
#             EXPLANATION: pronoun, personal

#             TOKEN: plays
#             =============================================================
#             TAG: VBZ        POS: VERB
#             EXPLANATION: verb, 3rd person singular present

#             TOKEN: an
#             =============================================================
#             TAG: DT         POS: DET
#             EXPLANATION: determiner

#             TOKEN: important
#             =============================================================
#             TAG: JJ         POS: ADJ
#             EXPLANATION: adjective (English), other noun-modifier (Chinese)

#             TOKEN: role
#             =============================================================
#             TAG: NN         POS: NOUN
#             EXPLANATION: noun, singular or mass

#             TOKEN: in
#             =============================================================
#             TAG: IN         POS: ADP
#             EXPLANATION: conjunction, subordinating or preposition

#             TOKEN: shaping
#             =============================================================
#             TAG: VBG        POS: VERB
#             EXPLANATION: verb, gerund or present participle

#             TOKEN: and
#             =============================================================
#             TAG: CC         POS: CCONJ
#             EXPLANATION: conjunction, coordinating

#             TOKEN: strengthening
#             =============================================================
#             TAG: VBG        POS: VERB
#             EXPLANATION: verb, gerund or present participle

#             TOKEN: global
#             =============================================================
#             TAG: JJ         POS: ADJ
#             EXPLANATION: adjective (English), other noun-modifier (Chinese)

#             TOKEN: architecture
#             =============================================================
#             TAG: NN         POS: NOUN
#             EXPLANATION: noun, singular or mass

#             TOKEN: and
#             =============================================================
#             TAG: CC         POS: CCONJ
#             EXPLANATION: conjunction, coordinating

#             TOKEN: governance
#             =============================================================
#             TAG: NN         POS: NOUN
#             EXPLANATION: noun, singular or mass

#             TOKEN: on
#             =============================================================
#             TAG: IN         POS: ADP
#             EXPLANATION: conjunction, subordinating or preposition

#             TOKEN: all
#             =============================================================
#             TAG: DT         POS: DET
#             EXPLANATION: determiner

#             TOKEN: major
#             =============================================================
#             TAG: JJ         POS: ADJ
#             EXPLANATION: adjective (English), other noun-modifier (Chinese)

#             TOKEN: international
#             =============================================================
#             TAG: JJ         POS: ADJ
#             EXPLANATION: adjective (English), other noun-modifier (Chinese)

#             TOKEN: economic
#             =============================================================
#             TAG: JJ         POS: ADJ
#             EXPLANATION: adjective (English), other noun-modifier (Chinese)

#             TOKEN: issues
#             =============================================================
#             TAG: NNS        POS: NOUN
#             EXPLANATION: noun, plural

#             TOKEN: .
#             =============================================================
#             TAG: .          POS: PUNCT
#             EXPLANATION: punctuation mark, sentence closer

#             TOKEN: India
#             =============================================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: holds
#             =============================================================
#             TAG: VBZ        POS: VERB
#             EXPLANATION: verb, 3rd person singular present

#             TOKEN: the
#             =============================================================
#             TAG: DT         POS: DET
#             EXPLANATION: determiner

#             TOKEN: Presidency
#             =============================================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: of
#             =============================================================
#             TAG: IN         POS: ADP
#             EXPLANATION: conjunction, subordinating or preposition

#             TOKEN: the
#             =============================================================
#             TAG: DT         POS: DET
#             EXPLANATION: determiner

#             TOKEN: G20
#             =============================================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: from
#             =============================================================
#             TAG: IN         POS: ADP
#             EXPLANATION: conjunction, subordinating or preposition

#             TOKEN: 1
#             =============================================================
#             TAG: CD         POS: NUM
#             EXPLANATION: cardinal number

#             TOKEN: December
#             =============================================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: 2022
#             =============================================================
#             TAG: CD         POS: NUM
#             EXPLANATION: cardinal number

#             TOKEN: to
#             =============================================================
#             TAG: IN         POS: ADP
#             EXPLANATION: conjunction, subordinating or preposition

#             TOKEN: 30
#             =============================================================
#             TAG: CD         POS: NUM
#             EXPLANATION: cardinal number

#             TOKEN: November
#             =============================================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: 2023
#             =============================================================
#             TAG: CD         POS: NUM
#             EXPLANATION: cardinal number

#             TOKEN: .
#             =============================================================
#             TAG: .          POS: PUNCT
#             EXPLANATION: punctuation mark, sentence closer