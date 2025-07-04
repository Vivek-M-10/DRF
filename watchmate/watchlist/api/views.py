
from asyncio import mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.views import APIView
from watchlist.models import Review, Watchlist, StreamPlatform  
from watchlist.api.serializers import WatchlistSerializer, StreamPlatformSerializer, ReviewSerializer

class ReviewList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class WatchlistView(APIView):
    def get(self, request):
        watchlist = Watchlist.objects.all()
        serializer = WatchlistSerializer(watchlist, many=True)
        return Response(serializer.data)

    def post(self, request):

        isbulk = isinstance(request.data, list)
        serializer = WatchlistSerializer(data=request.data, many=isbulk)
        if serializer.is_valid():
            watchlists = serializer.save()
            response_data = (
                WatchlistSerializer(watchlists, many= True).data
                if isbulk 
                else WatchlistSerializer(watchlists).data
            )
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WatchlistDetailView(APIView):
    def get(self, request, pk):
        try:
            watchlist_item = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchlistSerializer(watchlist_item)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            watchlist_item = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WatchlistSerializer(watchlist_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            watchlist_item = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        watchlist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class StreamPlatformView(APIView):
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        