from rest_framework import serializers
from django.contrib.auth.models import User
from prompts.models import (
    Prompt,
    Feature,
    Tag,
)


class TagSerializer(serializers.ModelSerializer):
        class Meta:
            model = Tag
            fields = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
        class Meta:
            model = Feature
            fields = '__all__'


class PromptSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    features = FeatureSerializer(many=True, source='feature_set', read_only=True)
    class Meta:
        model = Prompt
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    prompts = PromptSerializer(many=True, source='prompt_set')

    class Meta:
        model = User
        fields = ['id', 'username', 'prompts']
