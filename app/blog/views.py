from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def post_list(request):

    posts = Post.objects.all()

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

        user =User.objects.all()[0]

        post =Post.objects.create(
            author=user,
            title=request.POST.get('title'),
            text=request.POST.get('text'),

        )

        html = ('{} \n'
                '{}\n'
                '{}\n'.format(
            post.author, post.title,post.text
        )

                )


        return HttpResponse(html)

    return render(request, 'blog/post_create.html')