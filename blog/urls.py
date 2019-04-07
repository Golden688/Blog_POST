from django.conf.urls import url, include
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='blog-home'),

    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),

    url(r'^about/', views.about, name='blog-about'),

] 