documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

lower_docs = []
for i in documents:
	lower_docs.append(i.lower())
print(lower_docs)
no_puncs = []

import string

for i in lower_docs:
	no_puncs.append(i.translate(str.maketrans('', '', string.punctuation)))
#print(no_puncs)

preprocessed_docs = []

for i in no_puncs:
	preprocessed_docs.append(i.split(' '))


frequency_list = []

import pprint
from collections import Counter

for i in preprocessed_docs:
	frequency_list.append(Counter(i))
pprint.pprint(frequency_list)