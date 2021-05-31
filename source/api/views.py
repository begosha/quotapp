from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.permissions import SAFE_METHODS
from rest_framework import generics
from rest_framework.response import Response
from webapp.models import Quote
from api.serializers import QuotesListSerializer, QuoteDetailSerializer


class QuoteListView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuotesListSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = Quote.objects.all()
        else:
            queryset = Quote.objects.filter(status=True)
        return queryset

class QuoteCreateView(generics.CreateAPIView):
    serializer_class = QuotesListSerializer


class QuoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuoteDetailSerializer
    queryset = Quote.objects.all()
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = Quote.objects.all()
        else:
            queryset = Quote.objects.filter(status=True)
        return queryset


