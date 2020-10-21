from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Upload image view
@login_required
def image_post_view(request): 
  
    if request.method == 'POST': 
        form = ImgForm(request.POST, request.FILES) 
  
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save() 
            return redirect(reverse('top'))
    else: 
        form = ImgForm() 

    return render(request, 'img_post_form.html', {'form' : form, 'Title':'Добавить фото'})

# Success after uloading
#@login_required
#def success(request, post_id):

# View for main page: top of images
def display_top_of_images(request): 
  
    if request.method == 'GET': 
        ImgPosts = ImgPost.objects.all().order_by('-rating')[:10]

    return render(request, 'display_image_posts.html', {'image_posts' : ImgPosts, 'Title':'Главная страница'})

def up_rating(request): #Для повышения рейтинга нужно найти картинку
    if request.method == 'POST':
        #Img_id = request.POST.get("id", False)
        ImgPosts = ImgPost.objects.all()
        for Img in ImgPosts:
            print(Img.id)
            if request.GET.get(str(Img.id), False):
                Img.rating += 1
                Img.save()


    return redirect('/')

