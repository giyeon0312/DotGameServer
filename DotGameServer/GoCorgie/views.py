from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from .models import Player
from .serializers import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset=Player.objects.all()
    serializer_class=PlayerSerializer

    @list_route()
    def rank_players(self,request):
        rank=Player.objects.all().order_by('-score')

        page = self.paginate_queryset(rank)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(rank, many=True)
        return Response(serializer.data)