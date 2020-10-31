from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer


class PostList(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"server_response":"Everything is fine"}, status=status.HTTP_200_OK)

            # return Response(serializer.data, status=status.HTTP_200_OK)  # или так
        else:

            return Response({"server_response":"smth went wrong"}, status=status.HTTP_400_BAD_REQUEST)

            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # или так
