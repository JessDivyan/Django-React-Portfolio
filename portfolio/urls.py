from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectViewSet,
    BlogPostViewSet,
    TagViewSet,
    FilterByTagView,
)

# Initialize the DefaultRouter
router = DefaultRouter()
router.register(r"tags", TagViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"blogposts", BlogPostViewSet)

# Include the router URLs in the urlpatterns
urlpatterns = [
    path("", include(router.urls)),
    path("filter-by-tag/", FilterByTagView.as_view(), name="filter-by-tag"),
]
