import time
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

# Vote for image view
@login_required
def vote_for_image(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)

        if form.is_valid():
            vote = form.save(commit=False)
            vote.user = request.user

            # If changing vote or voting virst time
            current_vote = Vote.objects.filter(image = vote.image, user = vote.user)

            if not current_vote.exists():
                vote.set_vote()

            elif current_vote[0].vote != vote.vote:
                updating_vote = Vote.objects.get(image = vote.image, user = vote.user)
                updating_vote.set_vote(vote = vote.vote)         

    return redirect('/')

@login_required
def delete_image(request):
    if request.method == 'POST':
        img_id = request.POST['image']
        ImgPost.objects.filter(id=img_id).delete()
    return redirect('/user')

@login_required
def update_image(request):
    if request.method == 'POST':
        img_id = request.POST['image']
        ImgPost.objects.filter(id=img_id).delete()
    return redirect('/user')

@login_required
def public_image(request):
    if request.method == 'POST':
        id = request.POST.get('image')
        Img = ImgPost.objects.get(id=id)
        if Img:
            Img.published_date = time.strftime("%Y-%m-%d %H:%MZ", time.localtime())
            print("%Y-%m-%d %M:%SZ", time.localtime())
            Img.save()
    return redirect('/user')


# View for main page: top of images
def display_top_of_images(request): 
  
    if request.method == 'GET': 
        ImgPosts = ImgPost.objects.exclude(published_date=None).order_by('-rating')[:10]
        # print(len(ImgPost.objects.all()))1

    return render(request, 'display_image_posts.html', {'image_posts' : ImgPosts, 'Title':' Топ картинок по рейтингу'})


def display_latest_of_images(request):
    if request.method == 'GET':
        ImgPosts = ImgPost.objects.exclude(published_date=None).order_by('-published_date')
        # print(len(ImgPost.objects.all()))

    return render(request, 'display_all_ image_posts.html', {'image_posts': ImgPosts, 'Title': 'Самые новые картинки'})


def display_user_page(request):
    if request.method == 'GET':
        ImgPosts = ImgPost.objects.all().order_by('-published_date')
        author_name = "Ваша"
        # print(len(ImgPost.objects.all()))

    return render(request, 'user_page.html', {'image_posts': ImgPosts, 'Title': 'Ваша страница',
                                              'author_name': author_name})

def go_to_author_page(request):
    """
    Косяк исправлен костылем!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    """
    if request.method == 'POST':
        author_name = ImgPost.objects.get(id=request.POST["image"]).author
        print(author_name)
        ImgPosts = ImgPost.objects.all().filter(author=author_name)
        print(ImgPosts)
        print(len(ImgPosts))
    return render(request, 'user_page.html', {'image_posts': ImgPosts,
                    'Title': "Страница "+str(author_name), 'author_name': author_name})