from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import SAFE_METHODS
from rest_framework import generics
from rest_framework.response import Response
from webapp.models import Quote
from api.serializers import QuotesListSerializer, QuoteDetailSerializer


class QuoteListView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuotesListSerializer

class QuoteCreateView(generics.CreateAPIView):
    serializer_class = QuotesListSerializer

class QuoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuoteDetailSerializer
    queryset = Quote.objects.all()


