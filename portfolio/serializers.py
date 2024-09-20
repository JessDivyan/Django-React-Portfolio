from rest_framework import serializers
from .models import Project, BlogPost, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)  # Nested serialization for reading

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "tech_stack",
            "thumbnail",
            "tags",
            "link",
            "order",
        ]

    # def get_thumbnail(self, obj):
    #     request = self.context.get("request")
    #     if obj.thumbnail:
    #         return request.build_absolute_uri(obj.thumbnail.url)
    #     return None

    def create(self, validated_data):
        # Extract tags from validated data
        tags_data = validated_data.pop("tags")
        project = Project.objects.create(**validated_data)

        # Create or get existing tags and add them to the project
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data["name"])
            project.tags.add(tag)

        return project

    def update(self, instance, validated_data):
        # Extract tags from validated data
        tags_data = validated_data.pop("tags", None)

        # Update the project fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update tags if provided
        if tags_data:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(name=tag_data["name"])
                instance.tags.add(tag)

        return instance


class BlogPostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)  # Nested serialization for reading

    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "created_at", "tags", "published"]

    def create(self, validated_data):
        # Extract tags from validated data
        tags_data = validated_data.pop("tags")
        blog_post = BlogPost.objects.create(**validated_data)

        # Create or get existing tags and add them to the blog post
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data["name"])
            blog_post.tags.add(tag)

        return blog_post

    def update(self, instance, validated_data):
        # Extract tags from validated data
        tags_data = validated_data.pop("tags", None)

        # Update the blog post fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update tags if provided
        if tags_data:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(name=tag_data["name"])
                instance.tags.add(tag)

        return instance
