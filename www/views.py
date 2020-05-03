from django.shortcuts import render
from .models import MyModel
from django.views.generic import CreateView ,ListView

# Create your views here.
def home(request):
    return render (request ,'www/home.html')

#this is testing to see what will happen
##################################
class Tea (CreateView):
    model = MyModel
    fields = ['content']

class TeaList(ListView):
    model = MyModel
    template_name = 'www/listing.html'
    context_object_name = 'fow'
    ordering = '-content'
