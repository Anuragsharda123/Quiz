from django.shortcuts import render, redirect
from django.views import View

class Test_Questions(View):
    def get(self, request):
        return render(request, 'test.html')