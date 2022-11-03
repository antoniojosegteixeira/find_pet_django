from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from .models import Post
from accounts.serializers import CurrentUserPostsSerializer
from findpet.permissions import AuthorOrReadOnly


class PostListCreateView(
        generics.GenericAPIView,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # List all
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # Perform create: intercepts the creation (and add posts)
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)

    # Post
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDeleteView(
        generics.GenericAPIView,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # Retrieve single post
    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

        # Update
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

        # Delete
    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(['GET'])
@permission_classes([AuthorOrReadOnly])
def get_posts_for_current_user(request: Request):
    user = request.user
    serializer = CurrentUserPostsSerializer(instance=user)

    return Response(
        data=serializer.data,
        status=status.HTTP_200_OK
    )
