from django.shortcuts import render
import re

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')


def result(request):
    sentence = request.GET['sentence']
    wordList = re.findall('\w+',sentence)

    return render(request, 'result.html', {'fulltext':sentence, 'count':len(wordList), 'name_l':wordList})