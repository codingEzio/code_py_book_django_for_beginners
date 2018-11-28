from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    """
        About the listview (content-related)
    """

    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'  # templates related