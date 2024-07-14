from django.shortcuts import render, redirect
from django.views import View
from ..models.test import Test
from ..models.user import User
from ..models.result import Result
from ..models.student import Student

class Test_Series(View):
    def get(self, request):
        tests = Test.objects.all()
        attempted_test_ids = None
        try:
            user = User.objects.get(Email = request.session['user'])
            student = Student.objects.get(Email=user)
            attempted_test_ids = Result.objects.filter(Student=student).values_list('Test', flat=True)
            result = Result.objects.filter(Student=student)
        except:
            pass


        data = {
            'tests': tests,
            'attempted_test_ids': attempted_test_ids,
        }
        
        try:
            del request.session['test']
        except:
            pass
        return render(request, 'test_series.html', data)
    

    def post(self, request):
        
        test = request.POST.get('testid')
        
        print(test)
        try:
            if(request.session['user']):
               request.session['test'] = test
               return redirect('instruction')

        except:
            return redirect('login')