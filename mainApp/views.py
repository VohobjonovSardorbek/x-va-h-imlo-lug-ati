from django.shortcuts import render
from django.views import View
from .models import *


class Home_view(View):
    def get(self, request):
        search = request.GET.get('search')

        correct_word = None
        incorrect_words = None
        if search is not None:
            corrects = Correct.objects.filter(word=search.lower())
            if corrects.exists():
                correct_word = corrects.first()
                incorrect_words = Incorrect.objects.filter(correct=correct_word)
            else:
                incorrects = Incorrect.objects.filter(word=search.lower())
                if incorrects.exists():
                    incorrect_word = incorrects.first()
                    correct_word = incorrect_word.correct
                    incorrect_words = Incorrect.objects.filter(correct=correct_word)
                else:
                    if 'x' not in search.lower() and 'h' not in search.lower() and search.lower() != '':
                        correct_word = 'soz_yoq'
                    elif search.lower() == '':
                        correct_word = False
                    else:
                        correct_word = 'Mavjud emas!'
        context = {
            "correct_word": correct_word,
            "incorrect_words": incorrect_words,
            "search": search,
        }
        return render(request, 'index.html', context=context)

    def post(self, request):
        pass
