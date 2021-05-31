from rest_framework import serializers
from webapp.models import Quote


class QuoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('id', 'text', 'author', 'rating', 'email', 'status', 'created_at', 'updated_at')
        read_only_fields = ('id', 'author', 'rating','created_at', 'updated_at')

class QuotesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = ('id', 'text', 'rating', 'created_at')
        read_only_fields = ('id',)