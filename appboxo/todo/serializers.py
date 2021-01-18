from rest_framework import serializers

from .models import Todo, Category


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50, required=False)
    description = serializers.CharField(max_length=500, required=False)
    category_id = serializers.IntegerField(write_only=True, required=False)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=False)
    todos = TodoSerializer(source='get_todos', many=True, required=False)
    title = serializers.CharField(required=False)

    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'todos']

    def create(self, validated_data):
        todos = validated_data.pop('get_todos')
        category = Category.objects.create(**validated_data)
        for todo in todos:
            Todo.objects.create(category=category, **todo)
        return category

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        todos = validated_data.get('get_todos', [])
        for todo in todos:
            Todo.objects.create(category=instance, **todo)
        instance.save()
        return instance
