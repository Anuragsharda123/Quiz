from django.shortcuts import render, redirect
from ..models.question import Question
from ..models.answer import Answer
from ..models.test import Test
from django.views import View


class Test_Questions(View):
    def get(self, request):
        test = Test.objects.get(id=int(request.session['test']))
        
        questions = Question.objects.filter(Test=test).prefetch_related('question')
        data = {
            'test': test,
            'questions': questions,
            'timing': test.Timing
            }

            

        return render(request, 'test.html', data)