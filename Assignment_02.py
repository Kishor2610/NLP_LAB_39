# Assignment No_02
# Name:Kishor Arjun More
# Roll No_39
# Title: "Implementation of Bag of Words using Gensim"

# importing libraries
import gensim
from gensim.utils import simple_preprocess
from gensim import corpora

# get input
inp = ["""Many scientific algorithms can be expressed in terms of large matrix operations 
       (see the BLAS note above). Gensim taps into these low-level BLAS libraries, 
       by means of its dependency on NumPy. So while gensim-the-top-level-code is pure Python."""]

# tokens from input
tokens = []
for line in inp[0].split('.'):
    tokens.append(simple_preprocess(line, deacc=True))

# store into g_dict
g_dict = corpora.Dictionary(tokens)

# Count number of tokens
print("The dictionary has: " + str(len(g_dict)) + " tokens")
print(g_dict.token2id)
print("\n")

# Bag of Words
bow =[g_dict.doc2bow(t, allow_update = True) for t in tokens]
print("Bag of Words : ", bow)

#Output::

# The dictionary has: 37 tokens
#   {'above': 0, 'algorithms': 1, 'be': 2, 'blas': 3, 'can': 4, 'expressed': 5, 'in': 6, 
#       'large': 7, 'many': 8, 'matrix': 9, 'note': 10, 'of': 11, 'operations': 12, 
#       'scientific': 13, 'see': 14, 'terms': 15, 'the': 16, 'by': 17, 'dependency': 18, 
#       'gensim': 19, 'into': 20, 'its': 21, 'level': 22, 'libraries': 23, 'low': 24, 
#       'means': 25, 'numpy': 26, 'on': 27, 'taps': 28, 'these': 29, 'code': 30, 'is': 31, 
#       'pure': 32, 'python': 33, 'so': 34, 'top': 35, 'while': 36  }


# Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), 
#                   (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1)], [(3, 1), 
#                   (11, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 1), (24, 1), (25, 1), 
#                   (26, 1), (27, 1), (28, 1), (29, 1)], [(16, 1), (19, 1), (22, 1), (30, 1), (31, 1), (32, 1), 
#                   (33, 1), (34, 1), (35, 1), (36, 1)], []]