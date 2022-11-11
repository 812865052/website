from .models import Article
from .serializers import ArticleSerializer
from rest_framework import permissions
from django_filters import rest_framework
from rest_framework import viewsets

class ArticleViewSet(viewsets.ModelViewSet):
    # 用一个视图集替代ArticleList和ArticleDetail两个视图
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_fields = ['title', 'status']

    
    # 自行添加，将request.user与author绑定
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
        
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ReadOnlyModelViewSet仅提供list和detail可读动作
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
