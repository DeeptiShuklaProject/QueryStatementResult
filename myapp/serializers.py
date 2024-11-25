

from rest_framework import serializers
from .models import ProblemStatement, Tag, MasterData

class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag model."""
    class Meta:
        model = Tag
        fields = ['id', 'name']


class MasterDataSerializer(serializers.ModelSerializer):
    """Serializer for MasterData model."""
    class Meta:
        model = MasterData
        fields = ['id', 'title', 'description', 'data']


class ProblemStatementSerializer(serializers.ModelSerializer):
    """Serializer for ProblemStatement model."""
    result = serializers.ReadOnlyField()  # Result is read-only as it's computed and saved
    tags = TagSerializer(many=True, read_only=True)  # Serialize related Tag objects
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        write_only=True,
        source='tags'  # This links the tag_ids field to the `tags` ManyToManyField in the model
    )  # Allow setting tags using their primary keys
    master_data = MasterDataSerializer(read_only=True)  # Serialize related MasterData object
    master_data_id = serializers.PrimaryKeyRelatedField(
        queryset=MasterData.objects.all(),
        write_only=True,
        source='master_data'  # This links the master_data_id field to the `master_data` ForeignKey in the model
    )  # Allow setting MasterData using its primary key

    class Meta:
        model = ProblemStatement
        fields = [
            'id',
            'statement',
            'sql_query',
            'pandas_query',
            'pyspark_query',
            'result',
            'level',
            'tags',         
            'tag_ids',      
            'master_data',
            'master_data_id',
        ]
