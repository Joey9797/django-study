from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 전체 게시글 데이터 조회
        articles = Article.objects.all()
        # articles 는 django 에서만 쓸 수 있는 queryset 데이터 타입임
        # 때문에 우리가 만든 ModelSerializer로 이 데이터를 변환해줘야 한다.
        serializer = ArticleListSerializer(articles, many=True)
        # DRF 에서 제공하는 Response를 사용해 JSON 데이터를 리턴해줄거임
        # JSON 데이터는 serializer의 data 속성에 존재함
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # 게시글 생성
        # 사용자 입력 데이터를 받아서, serializing 해준다.
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        # 기존의 데이터 (article) 넣어주기
        # 새로운 사용자 입력 데이터 받아서 시리얼라이징 하기
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # 사용자가 이상한 데이터 입력 시 (유효성 검사 통과 못했을 시)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
