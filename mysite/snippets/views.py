from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):
    # 当我们的类视图继承了GenericAPIview，必须在定义的方法前，指定查询结果集和所要使用的序列化器
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    # temp = SnippetSerializer(queryset[0])
    
    # print(f"queryset:{queryset[0].created}")
    # # print(f"temp:{temp}")
    # print(f"serializer_class.data:{serializer_class.data}")
    # print(f"serializer_class:{serializer_class}")
    # # print(f"serializer_class属性:{dir(serializer_class)}")
    # print(f"serializer_class.fields:{serializer_class.get_fields()}")
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer