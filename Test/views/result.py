from django.shortcuts import redirect, render
from django.views import View
from ..models.answer import Answer
from ..models.question import Question
from ..models.student import Student
from ..models.test import Test
from ..models.user import User
from ..models.student_attempt import Student_Attempt

class Result(View):
    def get(self, request):
        return redirect('home')
    
    def post(self, request):

        user = User.objects.get(Email=request.session['user'])
        student = Student.objects.get(Email=user)
        test = Test.objects.get(id=int(request.session['test']))

        answers = {}
        for key in request.POST:
            if key.startswith('question'):
                question_id = key.replace('question', '')
                answers[question_id] = request.POST.getlist(key)[0]

        

        print("Hello",answers)
        
        for i,j in answers.items():
            question = Question.objects.get(id=int(i))
            ans = Answer.objects.get(id=int(j))
            student_attempt = Student_Attempt(Student=student, Test=test, Question=question, Answer=ans)
            

        return redirect('test_series')


def set_result():
    pass