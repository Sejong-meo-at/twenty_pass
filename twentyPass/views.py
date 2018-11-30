from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TwentyPass
from .forms import PostForm

# Create your views here.
def index(request):
    twentyPass = TwentyPass.objects.all()
    return render(request, 'twentyPass/index.html', {"twentyPass": twentyPass})

def detail(request, primaryKey):
    twentyPass = TwentyPass.objects.get(pk = primaryKey)
    twentyPass.question = twentyPass.question.replace('\n', '')
    q = twentyPass.question.split()
    return render(request, 'twentyPass/detail.html', {"q": q, "twentyPass": twentyPass})

def add(request):
    if request.method == "POST":
        #save data
        form = PostForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.update_dates()
            print('yes')
            print(question)
            return redirect('index')
        else:
            return redirect('add')
    else:
        form = PostForm()
        return render(request, 'twentyPass/form.html', {"form":form})
