from rest_framework import serializers
from .models import ProblemStatement, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class ProblemStatementSerializer(serializers.ModelSerializer):
    result = serializers.ReadOnlyField()
    # Serializing the related Tag objects using the TagSerializer
    tag = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        write_only=True,
        source='tag'
    )

    class Meta:
        model = ProblemStatement
        fields = ['id', 'statement', 'query', 'result', 'level', 'tag', 'tag_ids']
