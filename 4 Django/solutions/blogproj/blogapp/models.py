from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.CharField(max_length=500)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.blog_post.title + ' - ' + self.text



