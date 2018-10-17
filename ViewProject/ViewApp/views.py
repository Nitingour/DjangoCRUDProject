from django.shortcuts import render
from ViewApp.models import Book
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
'''def listView(request):
    books=Book.objects.all() # fatch data + templates send +Context set>>send data using dict.
    return render(request,"ViewApp/home.html",{'books':books})
'''

class ListViewDemo(ListView):
    model=Book

class DetailViewDemo(DetailView):
    model=Book

class CreateViewDemo(CreateView):
    model=Book
    fields='__all__'

class UpdateViewDemo(UpdateView):
    model=Book
    fields='__all__'

class DeleteViewDemo(DeleteView):
    model=Book
    success_url=reverse_lazy("home")
