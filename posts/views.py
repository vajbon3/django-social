from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.http import require_POST, require_http_methods
from django.views.generic import ListView, DetailView

from posts.models import Post, Photo


class PostList(ListView):
    model = Post
    ordering = ['-created_at']
    paginate_by = 5


class PostDetail(DetailView):
    model = Post
    ordering = ['-created_at']
    paginate_by = 5


@require_POST
def post_create(request):
    data = request.POST
    post = Post.objects.create(content=data['content'])
    # photos
    for file in request.FILES.getlist('photos'):
        photo = Photo.objects.create(image=file)
        post.photos.add(photo)
    post.save()
    return redirect(reverse('posts:post_list'))


@require_http_methods(['DELETE'])
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect(reverse('posts:post_list'))
