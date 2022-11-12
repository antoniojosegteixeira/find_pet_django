from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import PostSerializer, PostImageSerializer, PostSerializerWithImages, CreatedPostSerializer
from .models import Post, PostImage
from accounts.serializers import CurrentUserPostsSerializer
from findpet.permissions import AuthorOrReadOnly
from django.shortcuts import get_object_or_404


class PostListView(
        generics.GenericAPIView,
        mixins.ListModelMixin,
):
    serializer_class = PostSerializerWithImages
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    # List all
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostCreateView(
        generics.GenericAPIView,
        mixins.CreateModelMixin,
):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Perform create: intercepts the creation (and add posts)
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)

    # Post
    def post(self, request: Request, *args, **kwargs):
        serializer = self.create(request, *args, **kwargs)
        return Response(data={'id': serializer.data["id"]})


class PostRetrieveUpdateDeleteView(
        generics.GenericAPIView,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AuthorOrReadOnly]

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


@api_view(['POST'])
@permission_classes([AuthorOrReadOnly])
def PostImageCreateView(request: Request):
    post_id = request.POST.get('post_id')
    if post_id is None:
        return Response(
            data={"error": "post_id is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    imagelist = []
    images = request.FILES.getlist('images')
    print(images)

    for image in images:
        print(image)
        serializer = PostImageSerializer(
            data={"image": image})

        if serializer.is_valid():
            post = get_object_or_404(
                Post, pk=post_id)
            serializer.save(post=post)
            imagelist.append(serializer.data)

        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    return Response(
        data=imagelist,
        status=status.HTTP_200_OK
    )
