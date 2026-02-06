from rest_framework import serializers

class CountryDetailSerializer(serializers.Serializer):
    name = serializers.CharField()
    capital = serializers.CharField()
    population = serializers.IntegerField()
    flag = serializers.CharField()
    region = serializers.CharField()

class CountryQuerySerializer(serializers.Serializer):
    name = serializers.CharField(required=True)