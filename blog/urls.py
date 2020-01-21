from django.urls import path
from . import views

#faz referencia a blog/views
urlpatterns = [
    path('', views.post_list, name = 'post_list'),  
]
