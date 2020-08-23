# from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request=request, template_name='home.html', context={'bird': 'crow'})


def display_word_count(request):
    fulltext = request.GET['fulltext']

    words_dict = {word: 0 for word in set(fulltext.split())}

    for word in fulltext.split():
        words_dict[word] = words_dict[word] + 1

    words_dict_list = sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request=request, template_name='words_counted.html', context={'fulltext': fulltext,
                                                                                'no_of_words': len(fulltext.split()),
                                                                                'wordsdictionary': words_dict_list})


def display_about_page(request):
    return render(request=request, template_name='about_page.html')
