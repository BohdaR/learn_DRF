from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Article
from main.serializers import MainSerializer


class MainAPIView(APIView):
    def get(self, requests):
        lst = Article.objects.all().values()
        return Response({'posts': MainSerializer(lst, many=True).data})

    def post(self, requests):
        serializer = MainSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'title': serializer.data})

    def put(self, requests, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Article.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})

        serializer = MainSerializer(data=requests.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, requests, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

# class MainAPIView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = MainSerializer
