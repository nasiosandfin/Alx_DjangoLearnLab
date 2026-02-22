from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/', views.PostListView.as_view(), name='posts'),
]

from django.urls import path
from . import views

urlpatterns = [
    # existing post routes...
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # comment routes (logical structure)
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_id>/comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-edit'),
    path('posts/<int:post_id>/comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]
