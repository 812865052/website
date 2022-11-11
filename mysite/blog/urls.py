# blog/urls.py
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', viewset=views.ArticleViewSet)
router.register(r'users', viewset=views.UserViewSet)

urlpatterns = [
    # re_path(r'^articles/$', views.ArticleList.as_view()),
    # re_path(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view()),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls