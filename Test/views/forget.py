from django.shortcuts import redirect, render
from django.core.mail import send_mail
from ..models.user import User
from django.views import View
from Quiz import settings
from random import randint

class Forget(View):
    def get(self, request):
        try:
            if (request.session['user']):
                return redirect('home')
        except:
                return render(request, 'forget.html')
        
    def post(self, request):
        Email = request.POST.get("email")
        error_message = None
        
        isExist = User.isExist(Email)

        if(not isExist):
             error_message = "User doesn't Exist"

        if error_message:
             return render(request, 'forget.html', {'error':error_message})
        
        obj = User.objects.get(Email = Email)
        otp = randint(100000,999999)
        request.session['otp'] = otp
        request.session['obj'] = obj.id

        subject = 'Password Reset'

        body = "Dear Student, \nYou have requested to reset the password for your Chemistry Test Prep account. Please find your One-Time Password (OTP) below:\n\n"+str(otp)+"\n\nThis OTP is valid for the next 10 minutes. If you did not request a password reset, please disregard this email.\nShould you require further assistance, please do not hesitate to contact our support team.\n\n\nKind regards, \nUtkarsh Academy Team"

        send_mail(subject, body, settings.EMAIL_HOST_USER, [obj.Email])

        return redirect('otp')