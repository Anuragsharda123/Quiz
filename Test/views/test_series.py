from django.views import View
from datetime import datetime
from ..models.test import Test
from ..models.user import User
from ..models.result import Result
from ..models.student import Student
from ..models.catagory import Catagory
from django.shortcuts import render, redirect

class Test_Series(View): 
    def get(self, request):
        c_id = Catagory.objects.all()[0].id
        current_time = datetime.now()
        
        try:
            if (request.GET.get('catagory_id')):
                c_id = request.GET.get('catagory_id')
                
        except:
            pass
        
        tests = Test.test_by_catagory(c_id)
        attempted_test_ids = None
        try:
            user = User.objects.get(Email = request.session['user'])
            student = Student.objects.get(Email=user)
            attempted_test_ids = Result.objects.filter(Student=student).values_list('Test', flat=True)
            
        except:
            pass

        catagory = Catagory.objects.all()
        data = { 
            'current_time': current_time,
            'check_catagory':int(c_id),
            'catagories':catagory,
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