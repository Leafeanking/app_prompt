from rest_framework import serializers
from prompts.models import (
    Prompt,
    Feature,
    Tag,
)


class TagSerializer(serializers.ModelSerializer):
        class Meta:
            model = Tag
            fields = '__all__'


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
        class Meta:
            model = Feature
            fields = '__all__'
