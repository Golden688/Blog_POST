from django.conf.urls import url, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='blog-home'),

    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),

    url(r'^post/new/$', PostCreateView.as_view(), name='post-create'),

    url(r'^about/', views.about, name='blog-about'),

] 