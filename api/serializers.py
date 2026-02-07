from rest_framework import serializers

class CountryDetailSerializer(serializers.Serializer):
    name = serializers.CharField()
    capital = serializers.CharField()
    population = serializers.IntegerField()
    flag = serializers.CharField()
    region = serializers.CharField()

class CountryQuerySerializer(serializers.Serializer):
    name = serializers.CharField(required=True)

class AgeQuerySerializer(serializers.Serializer):
    name = serializers.CharField(required=True)

class CountryUniversitiesQuerySerializer(serializers.Serializer):
    country = serializers.CharField(min_length=1,required=True)

class CountryUniversitiesSerializer(serializers.Serializer):
    country = serializers.CharField()

# class CountryUniversitySearchSerializer(serializers.Serializer):
