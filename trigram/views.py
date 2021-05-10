from django.shortcuts import render
import nltk
from nltk.tokenize import word_tokenize
from django.http import HttpResponse

# Create your views here.
tokens = []


def generateTrigram(request):
    words_freq = {}
    with open('trigram/politics.txt') as fin:
        tokens = word_tokenize(fin.read())

    trigrams = {}
    bigrams = {}
    for i in range(len(tokens) - 2):
        cur_seq = " ".join(tokens[i:i + 2])

        # print(cur_seq)
        if cur_seq not in trigrams:
            trigrams[cur_seq] = []
            bigrams[cur_seq] = 1
        else:
            trigrams[cur_seq].append(tokens[i + 2])
            bigrams[cur_seq] += 1
        # print("enter")
    # print(trigrams.values())
    # calculate freq of each word after i sentence
    trigrams_freq = {}
    for key in trigrams.keys():
        values = trigrams[key]
        trigrams_freq[key] = []
        for value in values:
            trigrams_freq[key].append((value, values.count(value)))
    trigrams_prop = {}
    # calculate prop of each word after i sentence
    for key in trigrams_freq.keys():
        trigrams_prop[key] = []
        value = trigrams_freq[key]
        for pair in value:
            trigrams_prop[key].append((pair[0], pair[1] / bigrams[key]))
    print(trigrams_prop)
    input = ""
    values = trigrams_prop[input]
    sorted(values, key=getKey)


def getKey(item):
    return item[1]
