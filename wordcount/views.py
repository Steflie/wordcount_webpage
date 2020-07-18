from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    """ Home page function """

    return render(request, 'home.html', {"request":request})


def count(request):
    """Count Words page"""

    # Get text
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    
    # Total number of words
    num_of_words = len(word_list)

    # Calculate each word's number of appearance
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # Add the word to dict
            word_dictionary[word] = 1
    
    # Sort the dict
    sorted_dict = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'num':num_of_words, 'word_dictionary':sorted_dict})


def about(request):
    """ Renders a page with about info """

    return render(request, 'about.html')

