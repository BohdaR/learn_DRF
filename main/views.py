from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Article
from main.serializers import ArticleSerializer


def article_view(request):
    return render(request, 'main/index.html')


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# class ArticleAPIList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleAPIUpdate(generics.UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleAPIView(APIView):
#     def get(self, requests):
#         lst = Article.objects.all().values()
#         return Response({'posts': ArticleSerializer(lst, many=True).data})
#
#     def post(self, requests):
#         serializer = ArticleSerializer(data=requests.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'title': serializer.data})
#
#     def put(self, requests, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Article.objects.get(pk=pk)
#         except:
#             return Response({"error": "Method PUT not allowed"})
#
#         serializer = ArticleSerializer(data=requests.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, requests, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = Article.objects.get(pk=pk)
#         except:
#             return Response({"error": "Method DELETE not allowed"})
#
#         instance.delete()
#         return Response({"post": "deleted"})

# class MainAPIView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = MainSerializer
