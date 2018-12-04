from django.contrib import admin


from .models import Article, Comment


class CommentInline(admin.TabularInline):
    """ The only difference here
        is the superclass being passed in :P

        Either `StackedInline` or `TabularInline`, 

        Well, I prefer the latter! Cleaner & nicer :) 
    """

    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


# well.. the orders here do matter to the execution!
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
