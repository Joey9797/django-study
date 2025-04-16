from rest_framework import serializers
from .models import Article

# 다중 데이터 (article list) 를 직렬화한다.
# 게시글의 일부 필드를 직렬화 하는 클래스
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

# 단일 데이터 (list) 를 직렬화한다.
# 게시글의 전체 필드를 직렬화 하는 클래스
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'