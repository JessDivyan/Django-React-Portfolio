from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache


# Serve the React app's index.html as a template
index_view = never_cache(TemplateView.as_view(template_name="index.html"))

urlpatterns = [
    path("admin/", admin.site.urls),  # Admin site URL
    path("api/", include("portfolio.urls")),  # Include the portfolio app URLs
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    re_path(r"^(?:.*)/?$", index_view),
]
