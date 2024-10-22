from django.urls import path

from posts import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('', views.post_create, name='post_create'),
    path('<int:pk>', views.post_delete, name='post_delete'),
]