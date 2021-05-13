from django.shortcuts import render, redirect, get_object_or_404
from .models import Log
from django.utils import timezone
from .forms import LogForm

# Create your views here.

def home(request):
    allPost = Log.objects.all()
    postNum = Log.objects.count()
    return render(request, 'home2.html', {'allPost': allPost})

def detail(request, id):
    blogPost = get_object_or_404(Log, pk = id)
    return render(request, 'detail2.html', {'blogPost':blogPost})
    
def new(request):
  if request.method == 'POST':
    form = LogForm(request.POST, request.FILES)
    if form.is_valid():
      new_blog = form.save(commit=False)
      new_blog.upload_date = timezone.now()
      new_blog.save()
      return redirect('o-log/detail', new_blog.id)
    return redirect('o-log/home')
  else:
    form = LogForm()
    return render(request, 'new2.html', {'form': form})
    

def edit(request, id):
  post = get_object_or_404(Log, pk = id)
  if request.method == 'GET': 
    blog_form = LogForm(instance = post)
    return render(request, 'edit2.html', {'edit_form':blog_form})
  else: 
    blog_form = LogForm(request.POST, request.FILES, instance = post)
    if blog_form.is_valid():
      edit_blog = blog_form.save(commit=False)
      edit_blog.upload_date = timezone.now()
      edit_blog.save()
    return redirect('/log/observation/'+str(id))


def delete(request, id):
  delete_review = Log.objects.get(id = id)
  delete_review.delete()
  return redirect('o-log/home')
