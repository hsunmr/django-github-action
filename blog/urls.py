from django.urls import path
from .views.blog import BlogView

urlpatterns = [
    path('', BlogView.as_view(), name="blog.index")
]
