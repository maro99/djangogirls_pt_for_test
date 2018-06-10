from django.conf.urls import url

from blog.views import post_list, post_detail

urlpatterns = [

    url(r'^$' ,post_list,name='post-list'),
    url(r'^(\d+)/',post_detail,name= 'post-detail'),
]

