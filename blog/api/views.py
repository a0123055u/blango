from rest_framework import generics

from blog.api.serializers import PostSerializer, UserSerializer
from blog.models import Post
from blog.api.permission import AuthorModifyOrReadOnly
from blango_auth.models import User
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer
from rest_framework import generics, viewsets

from blog.api.serializers import (
    PostSerializer,
    UserSerializer,
    PostDetailSerializer,
    TagSerializer,
)
from blog.models import Post, Tag


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     permission_classes = [AuthorModifyOrReadOnly]
#     serializer_class = PostSerializer
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly ]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    authentication_classes = [SessionAuthentication]
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer



class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [SessionAuthentication]
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "create"):
            return PostSerializer
        return PostDetailSerializer

from rest_framework.decorators import action
from rest_framework.response import Response


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(methods=["get"], detail=True, name="Posts with the Tag")
    def posts(self, request, pk=None):
        tag = self.get_object()
        post_serializer = PostSerializer(
            tag.posts, many=True, context={"request": request}
        )
        return Response(post_serializer.data)
