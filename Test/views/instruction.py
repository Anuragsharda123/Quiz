from django.shortcuts import redirect, render
from django.views import View

class Instruction(View):
    def get(self, request):
        return render(request, "instruction.html")