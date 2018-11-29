from django.db import models
from django.urls import reverse


class Post(models.Model):
    """
        Let's create the basic component for the 'blog' app!

        There's a hidden (auto-incremented) id among us!!! (XD)
        It was used as 'primary-key' btw.
    """

    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ It enables us to `submit then redirect` to the right page 
        """

        return reverse("post_detail", args=[str(self.id)])
