from django.shortcuts import render
from .models import Library

# Create your views here.

def index(request):

    # import all the photos and save it in the db
    photo = Library.objects.all()
    context = {'photo':photo}
    return render(request, 'photo/index.html', context)
