from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def post_list(requst):

    return HttpResponse('post-list-page')