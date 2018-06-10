from django.conf.urls import url

from blog.views import post_list

urlpatterns = [

    url(r'^$' ,post_list)

]