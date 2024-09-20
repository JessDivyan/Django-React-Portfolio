from rest_framework import viewsets, filters
from .models import Project, BlogPost, Tag
from .serializers import ProjectSerializer, BlogPostSerializer, TagSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'tech_stack', 'tags__name']
    ordering_fields = ['title', 'tech_stack', 'order']

    def perform_create(self, serializer):
        # Handle creating projects with nested tags
        serializer.save()

    def perform_update(self, serializer):
        # Handle updating projects with nested tags
        serializer.save()

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'tags__name']
    ordering_fields = ['created_at', 'author']

    def get_queryset(self):
        # Override to filter by 'published' status
        queryset = super().get_queryset()
        is_published = self.request.query_params.get('published')
        if is_published is not None:
            queryset = queryset.filter(published=is_published.lower() == 'true')
        return queryset

    def perform_create(self, serializer):
        # Handle creating blog posts with nested tags
        serializer.save()

    def perform_update(self, serializer):
        # Handle updating blog posts with nested tags
        serializer.save()


class FilterByTagView(APIView):
    def get(self, request, *args, **kwargs):
        tag_name = request.query_params.get('tag')
        if not tag_name:
            return Response({"error": "Tag parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Filter projects and blog posts by tag
        projects = Project.objects.filter(tags__name=tag_name)
        blog_posts = BlogPost.objects.filter(tags__name=tag_name)

        # Serialize the data
        project_serializer = ProjectSerializer(projects, many=True)
        blog_post_serializer = BlogPostSerializer(blog_posts, many=True)

        # Combine results
        result = {
            "projects": project_serializer.data,
            "blog_posts": blog_post_serializer.data
        }

        return Response(result, status=status.HTTP_200_OK)
    
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# # Optional: You can customize TokenObtainPairView if needed
# class CustomTokenObtainPairView(TokenObtainPairView):
#     pass

# class CustomTokenRefreshView(TokenRefreshView):
#     pass
