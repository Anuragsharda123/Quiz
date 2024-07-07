from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from ..models.student import Student
from ..models.user import User
from django.views import View

class Login(View):
    def get(self, request):
        try:
            if(request.session['user']):
                return redirect('home')
        except:
            return render(request, 'login.html')
                
    
    def post(self, request):
        Email = request.POST.get('email')
        Password = request.POST.get('password')


        def isExist(Email):
            try:
                if (User.objects.get(Email=Email) and Student.objects.get(Email=(User.objects.get(Email=Email)))):
                    return True
            except:
                return False
            
        if(isExist(Email)):
            user = User.objects.get(Email=Email)
            flag = check_password(Password, user.Password)
            
            if(flag):
                request.session['user'] = Email
                return redirect('home')
            

def Logout(request):
    try:
        request.session.clear()
        return redirect('login')
    except:
        return redirect('login')


