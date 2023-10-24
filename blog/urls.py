from django.urls import path, include
from .views.blog import BlogView

urlpatterns = [
    path('', BlogView.as_view(), name="blog.index")
]
