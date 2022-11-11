from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model

User = get_user_model()

def title_gt_90(value):
    if len(value) < 10:
        raise serializers.ValidationError('标题字符长度不低于90。')

class UserSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'articles',)
        read_only_fields = ('id', 'username',)

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True) # required=False表示可接受匿名用户，many=True表示有多个用户。
    status = serializers.ReadOnlyField(source="get_status_display")
    cn_status = serializers.SerializerMethodField()
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    title = serializers.CharField(validators=[title_gt_90])

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')

    def get_cn_status(self, obj):
        if obj.status == 'p':
            return "已发表"
        elif obj.status == 'd':
            return "草稿"
        else:
            return ''
        
    def validate_title(self, value):
        """
        Check that the article is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Article is not about Django")
        return value
    
    
class EventSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data