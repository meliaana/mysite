from django.urls import path
from .views import PostListView, PostDitailView, PostCreateView, PostUpdateView, PostDeleteView, AddCommentView, UserPostListView
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>", PostDitailView.as_view(), name="post-detail"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/comment", AddCommentView.as_view(), name="post-comment"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("about/", views.about, name="blog-about"),

]
