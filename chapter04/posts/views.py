from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    """
        `ListView` is for displaying content.
        `all_posts_list` is for templates (db <-> frontend)
    """

    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'  # templates related