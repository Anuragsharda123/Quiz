from django.shortcuts import render, redirect
from django.views import View
from ..models.test import Test
from ..models.question import Question

class Test_Series(View):
    def get(self, request):
        tests = Test.objects.all()
        data = {
            'tests':tests
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