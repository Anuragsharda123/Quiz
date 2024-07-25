from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from ..models.student import Student
from ..models.user import User
from django.views import View


class OTP(View):
    def get(self, request):
        try:
            if request.session['otp']:
                return render(request, 'otp.html')
        
        except:
            try:
                if request.session['user']:
                    return redirect('home') 
            except:
                return redirect('home')
            
    def post(self, request):
        otp = int(request.POST.get('otp'))
        print(otp)
        print(request.session['otp'])
        error_message = None

        flag =  request.session['otp'] == otp
        request.session['flag'] = flag
        if flag:
            del request.session['otp']
            return redirect('reset_password')
        else:
            error_message = "Incorrect OTP"
            return render(request, 'e_send_otp.html',{"error":error_message})
        


class ResetPassword(View):
    def get(self, request):
        try:
            if request.session['user']:
                return redirect('home')
        except:
            try:
                if request.session['otp']:
                    return redirect('login')
            except:
                try:
                    if request.session['flag']:
                        return render(request, 'reset_password.html')
                except:
                    return redirect('home')
                
    def post(self, request):
        error_message = None
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpass')
        # print(request.session['eobj'])
        
        if (password != confirm_password):
            error_message = "Confirm Password Mismatch"

        if error_message:
            return render(request, 'reset_password.html',{"error":error_message})
        
        try:
            obj = request.session['obj']
            user = User.objects.get(id=int(obj))
            user.Password = make_password(password)
            user.save()
            return redirect('login')
        except:
            print(error_message)
            return render(request, 'reset_password.html',{"error":error_message})