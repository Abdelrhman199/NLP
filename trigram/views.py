from django.shortcuts import render
import nltk
from nltk.tokenize import word_tokenize
from django.http import HttpResponse
import json


# nltk.download('punkt')


# Create your views here.
def index(request):
    return render(request, 'index.html')


def generate_trigram(request):
    # return HttpResponse(request.GET['text'])
    with open('trigram/politics.txt', encoding='windows-1256') as fin:
        tokens = word_tokenize(str(fin.read()))

    # print(tokens)
    trigrams = {}
    bigrams = {}
    for i in range(len(tokens) - 2):
        cur_seq = " ".join(tokens[i:i + 2])
        if cur_seq not in trigrams:
            trigrams[cur_seq] = []
            bigrams[cur_seq] = 1
        else:
            trigrams[cur_seq].append(tokens[i + 2])
            bigrams[cur_seq] += 1
    trigrams_freq = {}
    for key in trigrams.keys():
        values = trigrams[key]
        trigrams_freq[key] = []
        for value in values:
            trigrams_freq[key].append((value, values.count(value)))
    trigrams_prop = {}
    for key in trigrams_freq.keys():
        trigrams_prop[key] = []
        value = trigrams_freq[key]
        for pair in value:
            trigrams_prop[key].append((pair[0], pair[1] / bigrams[key]))
    # print(trigrams_prop)
    input = request.GET['text']
    # print("input: ", input)
    if input in trigrams_prop.keys():
        values = trigrams_prop[input]
        if len(values) != 0:
            sorted(values, key=get_key, reverse=True)
            response = json.dumps(values, ensure_ascii=False)
            return HttpResponse(response)
        else:
            return HttpResponse('No results')
    else:
        return HttpResponse('No results')


def get_key(item):
    return item[1]
