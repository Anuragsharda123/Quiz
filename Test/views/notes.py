from django.shortcuts import render, redirect
from django.views import View
from ..models.note import Notes as Note

class Notes(View):
    def get(self, request):
        notes = Note.objects.all()
        return render(request, "notes.html" , {'notes':notes})