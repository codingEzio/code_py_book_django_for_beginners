# Chapter 05 (why name it? cuz there's cp06 down below)

### steps (initial phase)
- okay 
    1. project & app 
    2. let Django know the new app: ```blog.apps.BlogConfig```
- then 
    1. add what we need to ```blog/models.py```
    2. generate detailed *models* 
        1. ```./manage.py makemigrations``` **blog**
        2. ```./manage.py migrate``` **blog**
    3. create an admin ```./manage.py createsuperuser```
    4. register the app in ```blog/admin.py``` (should be done early!!)
- and the routines (urls, views etc.)
    - urls 
        - proj level, app level
    - views
        - related: model, template 
            - template: PROJ/templates
                1. base.html
                2. home.html 


### new thing: **static files**
- initial 
    - make A DIR (proj level) e.g. 
        - proj
        - proj/static
        - proj/static/css
        - proj/static/css/***base.css**
- really add some styles 
    1. static folder created (& files of course) 
    2. let Django *knows* where it is (declare in ```settings.py```
        - type ```STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]``` 
    3. load it into template
        - at top: ```load static```
        - header: ```<link href="{% static 'css/base.css' %}" rel="stylesheet">```

- something more 
    1. ```DetailView``` in ```views.py```
        - by default it'll provide a context object 
            - either ```object``` or lowercase of our ***model***
        - and *expects* either 
            - a *primary key* or a ?*slug passed to it as the identifier* (wtf) ("more on this shortly" said by author)

- let's talk about ```class in views```
    - e.g. ```BlogListView```, ```BlogDetailView```
        1. inside, its model (name) is ```Post``` (which was imported from the ```models.py``` file)
        2. and ***we're using the in the template***
    - about the "how we're using the name"
        - (we've talked about that, but to be clear, I gonna say it again)
    - it's either ```object``` OR the model name ```post``` 
        - like the name were used in the ```home.html```
            1. ```for post in object_list```
            2. ```post.titl```
            3. ```post.body```
    - BUT! We're gonna change it (by adding another ***static variable***)
        - thus ```context_object_name```


- about the ```post/<int:pk>/``` in the (APP) ```blog/urls.py```
    1. ```post/```: starts with [post/](post/)
    2. other than the three **col** (i.e. ```title```, ```author```, ```body```) defined in the ```models.py``` => class ```Post```
        - the Django itself create a ```id``` col for us (it was used as our ***primary-key***)
        - the ```pk``` is exactly *points* to that (aha!) (it's *auto-increment*, BTW 😅)

- one last step
    - give the ```href``` the real power! (points to actual post)
        - (it was '#' before)
    - edit the ```home.html```
        - before 
            - ```<h2><a href=```
        - now
            - ```<h2><a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a></h2>```

<hr>

# Here comes the 'chapter06' (which based on the 'Chapter05' project)

### forms! 
- that's a security concern: **CSRF** 
    - we'll talk about later (Page 128) 
    - ... and notes will be take later as well :P
  
### still, we'need to know what was added in Chapter 06 (at least part of them)
- okay.. 
    1. add new function to ```base.html``` first (that we didn't impl it, yet.)
        - like ```<a href="{% url 'post_new' %}">+New blog post</a>```
    2. add **url**
        - ```path('post/new/', BlogCreateView.as_view(), name='post_new')```
    3. add **view**
        - ```from django.views.generic.edit import CreateView```
        - ```class BlogCreateView(CreateView):``` ... 
    4. and we go back to the *template* (in ```views.py```, we don't impl yet when creates it)
        - that is```template_name = 'post_new.html'```
        - so let's impl the template! 
- now we've impl it, but cannot *submit* then **redirect** to the right page
    - do this (in ```models.py```)
        1. ```from django.urls import reverse```
        2. ```def get_absolute_url(self):  return reverse("post_detail", args=[str(self.id)])```


### Now we'll add a new func (Form::editPost)
- steps 
    1. add entry <post_edit> in post_detail (both're tmplts)
    2. write post_edit   
        1. then its views 
        2. then its urls #TODO edit later
- let's talk about the deletePost here as well
    1. add entry (i.e. a link) in post_detail 
    2. write post_delete (similar, but not the same as 'post_edit')
        1. then its views 
        2. then its urls #TODO edit later 


### Okay! Let's writing tests! 
- other than the tests we've written before, we need these 
    1. test_get_absolute_url #TODO add 'code' fmt (and the rest of them)
    2. test_post_create_view
    3. test_post_create_view
    4. test_post_create_view
- more content (& description) was written inside the tests.py #TODO code fmt