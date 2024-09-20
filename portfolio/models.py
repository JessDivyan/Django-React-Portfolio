from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    tags = models.ManyToManyField(Tag, related_name='projects')
    link = models.URLField(max_length=200, blank=True, null=True)  # Optional link field
    order = models.IntegerField(blank=True, null=True)  # Optional order field

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    published = models.BooleanField(default=False)  # Field to control if the blog post is published

    def __str__(self):
        return self.title
