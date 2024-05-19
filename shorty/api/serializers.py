from rest_framework import serializers

from shortener.models import URL, URLEncodeMedium

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['full_url', 'url_hash']

class HashURLSerializer(serializers.Serializer):
    full_url = serializers.URLField()

    def create(self, validated_data):
        query_set = URL.objects.create(**validated_data, medium=URLEncodeMedium.API)
        return query_set