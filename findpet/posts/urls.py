from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view()),
    path("create/", views.PostCreateView.as_view()),
    path("<int:pk>/", views.PostRetrieveUpdateDeleteView.as_view()),
    path("current_user/", views.get_posts_for_current_user, name="current_user"),
    path("image/", views.PostImageCreateView, name="image")
]
