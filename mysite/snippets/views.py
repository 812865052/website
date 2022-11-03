from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers


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
        print(serializer)
    


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
    
    
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
    
    
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)