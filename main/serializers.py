from typing import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from main.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


# class MainSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_created = serializers.DateTimeField(read_only=True)
#     time_updated = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_updated = validated_data.get("time_created", instance.time_updated)
#         instance.is_published = validated_data.get("time_updated", instance.is_published)
#         instance.cat_id = validated_data.get("is_published", instance.cat_id)
#         instance.save()
#         return instance


# class MainModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# def encode():
#     model = MainModel('Some title', 'Some content')
#     model_sr = MainSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesI0(b'{"title": "Angelina Jolie","content":"Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = MainSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)


# class MainSerializer(serializers.Serializer):
#     class Meta:
#         model = Article
#         fields = ('title', 'cat_id')
