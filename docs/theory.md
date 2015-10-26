
## Reverse Dictionary

Given a  phrase, find a word that best summarizes it.

#### Challenges

1. sue       =>  to take legal actions against
2. depravity =>  moral corruption
3. demur     =>  disagree to obey/ to refuse to take orders/ disobedience/ to object/ to refuse/
4. Pandiculation => stretching oneself's body just after waking up, or when feeling drowsy.
5. Petrify => To convert, as any animal or vegetable matter, into stone or stony substance.

### Indicators

1. Morphemes - morphological analysis
2. Synsets in wordnet: A synset represents coarsely "one sense"; 
3. Affixes
4. 





### Components
1. Phrase similarity / semantic similarity
2. Word similarity



### Method 1:

```
* Initialize score[word] = 0 for every word in the dictionary
* For every word a in score:
		score[a] = - sum(distance between a and b in thesarus for every word b in phrase)
```

### Method 2:

Find the gloss of every word in the dictionary. Check its semantic similarity against the
input phrase. Return the words with the highest scores.
The words constituting the glosses and the input phrase may have different senses. So, we either
consider all the senses or disambiguate them while checking for semantic similarity.




