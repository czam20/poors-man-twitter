from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import TweetSerializer
from .models import Tweet

class TweetViewSet(ModelViewSet):
    """Tweet view set"""
    serializer_class = TweetSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return Tweet.objects.all()
        return Tweet.objects.get(id=pk)

    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_tweets = self.get_serializer(queryset, many=True)

        if request.method == 'POST':
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return render(request, 'index.html', {'tweets': serializer_tweets.data})
            else:
                return render(request, 'index.html', {'tweets': serializer_tweets.data, 'error': serializer.errors})


        return render(request, 'index.html')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        return render(request, 'index.html', {'tweets': serializer.data})
