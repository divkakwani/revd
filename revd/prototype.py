#!/bin/env python

import nltk
from nltk import wordnet as wn

# TODO: add full dict later
dictionary = ['bigot', 'demur', 'pandiculation', 'perpetuate', 'pedantic', 'euphemism',
              'petrify', 'adage', 'resentment', 'aglet']


from nltk.tokenize import RegexpTokenizer

# use jcn_similarity, lin_similarity or res_similarity
def word_semantic_similarity(word1, word2):
    """ """
    synsets1 = wn.wordnet.synsets(word1)
    synsets2 = wn.wordnet.synsets(word2)

    score = max(s1.path_similarity(s2) for s1 in synsets1 for s2 in synsets2)
    if score == None:   score = 0

    return score

def phrase_semantic_similarity(phrase1, phrase2):
    """ """
    # FIXME: Use maximum bipartite matching.

    stopwords = nltk.corpus.stopwords.words('english')
    tokenizer = RegexpTokenizer(r'\w+')

    wordlist1 = list(w for w in tokenizer.tokenize(phrase1) if w not in stopwords)
    wordlist2 = list(w for w in tokenizer.tokenize(phrase2) if w not in stopwords)
    
    # score matrix - score[i][j] = similarity between wordset1[i] and wordset2[j]
    score = [[word_semantic_similarity(w1, w2) for w2 in wordlist2] for w1 in wordlist1]

    p1_score = sum(max(score[i]) for i in range(len(wordlist1)))/len(wordlist1)
    p2_score = sum(max(score[i]) for i in range(len(wordlist2)))/len(wordlist2)
    avg_score = (p1_score + p2_score)/2.0

    return avg_score


def score_word_meaning(word, phrase):
    """ """
    synsets = wn.wordnet.synsets(word)  # Find all the senses of `word`
    glosses = [s.definition() for s in synsets]
    return max(phrase_semantic_similarity(gloss, phrase) for gloss in glosses)


def reverse_dict_lookup(phrase):
    """Returns a word in the dictionary closest in meaning to the input phrase."""
    scores = [score_word_meaning(word, phrase) for word in dictionary]
    return dictionary[max(range(len(dictionary)), key=lambda i: scores[i])]


while True:
    print 'Enter a phrase: '
    phrase = raw_input()
    print 'The closest word for the phrase is: ', reverse_dict_lookup(phrase)


