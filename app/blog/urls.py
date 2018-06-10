from django.conf.urls import url

from blog.views import post_list, post_detail, post_create, post_delete

urlpatterns = [

    url(r'^$' ,post_list,name='post-list'),
    url(r'^(\d+)/$',post_detail,name= 'post-detail'),
    url(r'^write/$',post_create, name = 'post-create'),
    url(r'^(\d+)/delete/$',post_delete,name = 'post-delete')
]

