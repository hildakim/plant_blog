from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm

# Create your views here.

def home(request):
    allPost = Blog.objects.all()
    return render(request, 'home.html', {'allPost': allPost})

def detail(request, id):
    blogPost = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blogPost':blogPost})
    
def new(request):
  if request.method == 'POST':
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
      new_blog = form.save(commit=False)
      new_blog.upload_date = timezone.now()
      new_blog.save()
      return redirect('detail', new_blog.id)
    return redirect('home')
  else:
    form = BlogForm()
    return render(request, 'new.html', {'form': form})

# def create(request):
#     form = BlogForm(request.POST, request.FILES)
#     if form.is_valid():
#         new_review = form.save(commit=False)
#         new_review.upload_date = timezone.now()
#         new_review.save()
#         return redirect('detail', new_review.id)
#     return redirect('home')
    

def edit(request, id):
  post = get_object_or_404(Blog, pk = id)
  if request.method == 'GET': 
    blog_form = BlogForm(instance = post)
    return render(request, 'edit.html', {'edit_form':blog_form})
  else: 
    blog_form = BlogForm(request.POST, request.FILES, instance = post)
    if blog_form.is_valid():
      edit_blog = blog_form.save(commit=False)
      edit_blog.upload_date = timezone.now()
      edit_blog.save()
    return redirect('/blog/post/'+str(id))


# def update(request, id):
#     update_review = Blog.objects.get(id = id)
#     update_review.review_title = request.POST['review_title']
#     update_review.nickname = request.POST['review_writer']
#     update_review.movie = request.POST['movie']
#     update_review.review_body = request.POST['review_body']
#     update_review.upload_date = timezone.now()
#     update_review.save()
#     return redirect('detail', update_review.id)

def delete(request, id):
  delete_review = Blog.objects.get(id = id)
  delete_review.delete()
  return redirect('home')
