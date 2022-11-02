"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from invest import views

urlpatterns = [
    url(r'^invest/', include('invest.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^upload_script/$', views.uploadify_script, name='uploadify_script'),
    url(r'^delete_uploadfile/$', views.file_delete, name='file_delete'),
    # 如果执行python manage.py makemigrations snippets报django.db.utils.OperationalError: no such table: snippets_snippet
    # 需要把下面这行注销，原因未知，因为看报错信息发现是这里有问题
    url(r'^snippets/', include('snippets.urls')),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]