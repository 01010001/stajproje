from rest_framework import serializers
from .models import Developers, Projects, Teams, WorkingOn

# class DeveloperSerializer(serializers.ModelSerializer):
#     example_serializer_method = serializers.SerializerMethodField()
#     # projects = projectsSerializer(many=True, read_onl=True)
#     class Meta:
#         model = models.Developers
#         fields = '__all__'
#         # exclude = ["etc", "etc2"]
#         # read_only_fields = []
    
#     def get_example_serializer_method(self, object):
#         return "test example serializer"
    

class WorkingOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingOn
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    developers = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='developers_set')

    class Meta:
        model = Teams
        fields = '__all__'

class DeveloperSerializer(serializers.ModelSerializer):
    works = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Developers
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    developers = serializers.SerializerMethodField()

    class Meta:
        model = Projects
        fields = '__all__'

    def get_developers(self, obj):
        # Get all developers in the project with is_relation_active=True
        active_developers = Developers.objects.filter(
            project=obj,
            works__is_relation_active=True
        ).values_list('id', flat=True)
        return active_developers
