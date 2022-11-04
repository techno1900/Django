from django.urls import path
from . import views

urlpatterns = [
    path('',views.posts,name="posts"),
    path('singlepost/<str:pid>/',views.post,name="post"),
    path('create-form',views.createNewPost,name="create"),
    path('upate-form/<str:pid>/',views.updatePost,name="update"),
    path('delete/<str:pid>/', views.delete,name="delete")
]