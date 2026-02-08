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

class UniversitySerializer(serializers.Serializer):
    name = serializers.CharField()
    website = serializers.SerializerMethodField()

    def get_website(self, obj):
        return obj['web_pages'][0]

class CountryUniversitiesSerializer(serializers.Serializer):
    country =serializers.CharField()
    universities = UniversitySerializer(many=True)

    def to_representation(self, instance):

        country = instance[0].get('country')

        universities = UniversitySerializer(instance, many=True).data
        
        return {
            'country':country,
            'universities':universities
        }