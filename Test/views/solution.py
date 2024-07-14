from django.shortcuts import render, redirect
from ..models.test import Test
from ..models.question import Question
from django.views import View

class Solution(View):
    def get(self, request):
        return redirect('test_series')
    
    def post(self, request):
        try:
            t = request.POST.get('testid')
            test = Test.objects.get(id=t)

            questions = Question.objects.filter(Test=test).prefetch_related('question')

            return render(request, 'solution.html', {'questions':questions})
        except:
            return redirect('test_series')