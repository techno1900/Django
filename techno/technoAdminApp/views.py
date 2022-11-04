from django.shortcuts import render, redirect
from . models import postTable
from .form import createPost
def posts(request):
    database = postTable.objects.all()
    return render(request, 'index.html', {'database':database})


def post(request,pid):
    database = postTable.objects.get(id = pid)
    return render(request,'post.html', {'database':database})

def createNewPost(request):
    form = createPost()
    if request.method == "POST":
        form = createPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    return render(request, ('form.html'),{'form':form})

def updatePost(request,pid):
    database = postTable.objects.get(id = pid)
    form = createPost(instance=database)
    if request.method == "POST":
        form = createPost(request.POST, instance=database)
        if form.is_valid():
            form.save()
            return redirect('posts')
    return render(request, 'form.html', {'form':form})

def delete(request, pid):
    database = postTable.objects.get(id=pid)
    if request.method == "POST":
        database.delete()
        return redirect('posts')
    return render(request, 'del.html')

# Create your views here.
