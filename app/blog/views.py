from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Post


def post_list(request):

    posts = Post.objects.order_by('-created_date')

    context = {
        'posts':posts,
    }


    return render(request,'blog/post_list.html',context)

def post_detail(request, post_id):

    post = Post.objects.get(id = post_id)

    context={
        'post':post,
    }

    return render(request, 'blog/post_detail.html',context)


def post_create(request):

    if request.method == 'POST':


        Post.objects.create(
            author=request.user,
            title=request.POST.get('title'),
            text=request.POST.get('text'),
        )



        return redirect('post-list')

    return render(request, 'blog/post_create.html')


def post_delete(request,post_id):

    Post.objects.get(id=post_id).delete()

    return redirect('post-list')


def post_edit(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.method =='POST':
        title=request.POST.get('title')
        text=request.POST.get('text')

        post.title=title
        post.text=text
        post.save()

        return redirect('post-detail',post_id)
    else:


        context={
            'post':post,
        }
        return render(request,'blog/post_edit.html',context)