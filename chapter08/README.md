
# Chapter 08 (that's other chapter(s) down below)

### Custom User Model 
- It's just means:
    - in real life, the default option provided is not enough
    - customzing ur own which accomplish 
        - reach ur needs
        - more secure (as it should be)
- Ah, we still need Django, 
    - yet we're gonna use a simpler one: ```AbstractUser```
    

### Initial setup 
- initial 
    1. ```django-admin startproject``` **```newspaper_project```** ```.```
    2. ```python manage.py startapp``` **```users```**
- migrate?
    - not yet, we'll it after we created the ***customized user model***
- base 
    1. let Django "knows" the app: ```'users.apps.UsersConfig'``` (in ```settings.py```)


### Customizing user model
- ( Most notes were takin as comments (inside ```forms.py``` & ```admin.py```) )
- let django knows it as well 
    1. model class ```CustomUser``` in app/```models.py```
    2. ```AUTH_USER_MODEL = 'users.CustomUser'``` in proj/```settings.py```
- ah! let's create **forms**! 
    - first we'll make two types of *forms*
        1. ```UserCreationForm```
        2. ```UserChangeForm```
- and "registering" them on the ```admin.py```
    - in cmp to before, 
    - now we add a model **and** a *CustomUserAdmin* (addition to default)
- okay! we're ready to go!
    1. ***make some migrations*** first!!! 
        - ```./manage.py makemigrations users ```
        - ```./manage.py migrate```

    2. **create a superuser** (must've done the "migrate" first)
    3. now you can go inside the URL```/admin``` now! (unfinished yet)
- but that's not enough actually 
    - one more line! 
    - class CustomUserAdmin on ```admin.py```
    - ```list_display = ['email', 'username', 'age', 'is_staff', ]```
    
    
# Chapter 09 (based on Chapter 08) 

### Home comes the *User Authentication*!
- Okay...

### Wait! Let's creating some templates first :P
- **NEW CONCEPT**
    1. The *Django loader* looks for tmplts in a nested struc ***within each app***.
        - so it means that *if you wanna add templates (specific for the app)*
        - y'll need put it in APP_FOLDER/```templates/APP_FOLDER/TEMPLATES_FILE``` 
    2. Well, I'm just sayin', I won't impl this right away.
    3. (🐶) Here's another quote of author (🐶)
        > ... a project-level ```templates``` folder approach is cleaner & scales better ...
        
### and some templates & UX thoughts
- nothing new about templates
- the page being redirected to after user login successfully, where?
    - normally 'home' (i.e. homepage, sort of)
    - **where's "home" comes from**?
    - right here: PROJECT/APP_FOLDER/```urls.py``` ('name' param)

### Okay, we're gonna write some templates
- first,
    1. ```'DIRS': [os.path.join(BASE_DIR, 'templates')],``` in **settings.py**
    2. two lines in **settings.py** (add to the bottom)
        - ```LOGIN_REDIRECT_URL = 'home'```
        - ```LOGOUT_REDIRECT_URL = 'home'```
- second, the files & folders
    1. proj/*base.html*
    2. proj/*home.html*
    3. proj/*signup.html*
    4. proj/```templates/registration/```*login.html*
- third, related ```urls.py``` & ```views.py```
    - **PROJECT_newspaper_project**/```urls.py```
    - **APP_users/**```urls.py```
- third in details 
    1. proj/urls.py 
        - ```path('users/', include('users.urls')),```
        - ```path('users/', include('django.contrib.auth.urls')),```
        - ```path('', TemplateView.as_view(template_name='home.html'), name='home'),```
    2. app/urls.py
        - ```path("signup/", SignUpView.as_view(), name="signup"),``` (import needed)
    3. app/views.py
        - ```class SignUpView``` (while using the ```forms.py``` we've created before)
- fourth we'll add **one more option** (i.e. *email addr*) in **sign-up page**! 
    - change the two classes: ```CustomUserCreationForm``` & ```CustomUserChangeForm```
        - change both their subclass: ```Meta```
            - change the ```fields``` variable to 
                - ```fields = ('username', 'email', 'age', )```

    
# Chapter 10 (still based on Chapter 08) 

### Add some styles! 
- Here comes the **Bootstrap** !

### Initial setup
- get an "app" (i.e. 'pages') by 
    1. ```./manage.py startapp pages```
    2. add ```'pages.apps.PagesConfig',``` to **settings.py**
- update "urls" (i.e. **urls.py**)
    1. proj/urls.py
    2. app_pages/urls.py
- and then our "views" -> "templates" (kinda a cycle that'll go all along)
- What we're doin' (**FOR NOW**, ONLY **IN THIS CONTEXT** (i.e. 'get an pages app')) is 
    - *replacing the code-gen-homepage* => *templt-html-used-before* 

### bootstrap NOW? 
- *Nah*, let's **write tests first** that for the work we've done for now!!
- Writing them in the ```pages/tests.py```
    - just go check the test file :P 
    - there's new one in contrast to the tests we've written before (i.e. *forms*)

### YES, bootstrap NOW! 
- how we're gonna use it?
    1. dl the files 
    2. name the links (inside .html file)
- We'll firstly update the "base.html".
    - add related links of *css* and *javascript* 
    - it's all added inside (nothing complicated :P)
- so ... we've *"imported"* the files (```.css```, ```.js```)
    - now we could apply any styles to the elements 
        - (specifically other than the **base.html**)
    - e.g. we changed the button style of **login.html**
        - ```<button class="btn btn-success ml-2" type='submit'>Log In</button>```

### Let's talk about the **sign-up** page :P
- (specifically the 'password requirement' (or sayin' "help_text"), stylish concerns I assume)
- We're not tring to 'replace' (or sayin' "overwrite") the "help_text", 
    - instead, we're using a third-party modules named ***django-crispy-forms***
        - install it by ```pip3 install django-crispy-forms==1.7.2``` (the ver. is optional)
    - then let Django "knows" it by (**settings.py**)
        1. INSTALLED_APPS -> add ```'crispy_forms',``` 
        2. at the bottom -> add ```CRISPY_TEMPLATE_PACK = 'bootstrap4'``` 
- we can use it for our templates! (steps of modifying ```signup.html```)
    1. load it by ```{% load crispy_forms_tags %}``` (right after the ```extends```)
    2. changes 
        - before: ```{{ form.as_p }}```
        - after: ```{{ form | crispy  }}```

    
# Chapter 11 (still based on Chapter 08) 

### Now, we're gonna talk about "password change & reset" 
- "We" will mention both 
    1. the **built-in** 
    2. and **our-customized-version** (powered by Bootstrap) (plus *email service*)

### how you get there (ver: built-in)
- type URL/```users/password_change``` (it works, just to be clear)

### customize our own **password change**
- firstly, templates! 
    1. proj/```templates/registration/```**```password_change_form.html```**
    2. proj/```templates/registration/```**```password_change_done.html```**
- once u've written them, just refresh the page, it's done! 

### lastly, let's talk about the **password reset**
- quotes from author (*a reminder for myself*) (slightly changed a few words)
    1. ... *the steps (i.e. "reset") are similar to conf password change* ...
    2. ... *Django already provides a default impl that we'll use and then customize* ...

### we'll use the Djangos' first (**settings.py**)
- the basic usage
    1. add ```EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'``` to the bottom
    2. go to [Password reset](http://localhost:8000/users/password_reset/)
    3. typing the email addr which was used while registering (you might don't have it XD)
    4. check the terminal (e.g. ```runserver```)
    5. there should be an email sent from *Django* itself  
        - access the url it provided 
        - typing the new passwd, then it's all done 
    6. some notes here
        - ya always should provided ur email while registering (debug purposes!)
        - *Django* will NOT mistaken whose password will be changed (even there's an user was online (by cookie))
- and might add some styles, shall we?
    - four templates, please! 
        1. ```templates/registration/```**```password_reset_form.html```**
        2. ```templates/registration/```**```password_reset_done.html```**
        3. ```templates/registration/```**```password_reset_confirm.html```**
        4. ```templates/registration/```**```password_reset_complete.html```**
    - its exec orders (in users' perspective) 
        - form => access the reset url (type ur email)
        - done => notification (we've sent for ya)
        - confirm => typing new password (**link** provided by Django (**at terminal**))
        - complete => reset complete (still notification)


# Chapter 12 (still based on Chapter 08) 

### Emails! 
- Third-party service: [SendGrid](https://sendgrid.com/)

### Intro (by myself)
- When you've registered, go to [*Integrate using our Web API or SMTP Relay*](https://app.sendgrid.com/guide/integrate)
    - select the option: "SMTP Relay" (cuz it's easier for now, said by the author)

### Practical usage 
- first change the value of ```EMAIL_BACKEND``` in **settings.py**
    - to ```EMAIL_BACKEND = 'django.core.mail.backends.```**```smtp.```**```EmailBackend'```
- then add the config stuff (still write to the **settings.py**)
    - you actually should NOT add these directly (cuz that's NOT SAFE!)
    - we will place the vars here just to keep things simple :)
        - the things gonna be added 
            - ```EMAIL_HOST = 'smtp.sendgrid.net'``` 
            - ```EMAIL_HOST_USER = 'apikey'```
            - ```EMAIL_HOST_PASSWORD = ```*```THE_API_KEY```*
            - ```EMAIL_PORT = 587```
            - ```EMAIL_USE_TLS = True```
- then run the server 
    1. you need a (local) user got an (**real**) email addr (if not => create one!)
    2. now, you can go the reset-page: ```http://127.0.0.1:8000/users/password_reset/``` 
    3. type ur (true) email to test (**sendgrid-email-service**) whether it works or not 
    4. now you could go check the ur inbox!!! (got one? nice!!)
    5. then click the "Verify Integration" on the *sendgrid* page (optional I assume, but whatever 🐶)
- Till now, our "password-reset" got real service (i.e. *sending reset email*) as backend! 

### Custom emails (still continue the prev 'practical usage')
- note 
    1. my IP has been *throttled* (i.e. the reset-email cannot be sent out)
    2. so.. down below is just demenstration (typing code ...)
- still, the default content being sent definitely is provided by Django itself 
    - after all, it's just coooooooode! 
    - where is it exactly?
        - here (split into two parts)
            1. ```VIRTUAL_ENV/lib/python3.6/site-packages/django/contrib```
            2. ```/admin/templates/registration/password_reset_email.html```
- so let's start customizing our own, yo! 
    - both under ```templates/registration/```
        1. **```password_reset_email.html```**
        2. **```password_reset_subject.txt```**
    - now just go directly to the reset-page 
        - everything ... should be fine 🐤 I assume 🙈


# Chapter 13 (still based on Chapter 08) 

### Time to build out our real *Newspaper* app! 
- What should be added right now?
    1. an articles page where you can ***post articles***
    2. seting up permissions that only ***author*** of an article can ***edit*** (or ***delete*** it)
    3. other users could ***write comments*** on each article 

### Basic setup (**posting** at **admin**)
- Creating an app: 
    1. ```./manage.py startapp``` **```articles```**
    2. add ```'articles.apps.ArticlesConfig',``` to **settings.py**
- Preparing (i.e. writing) ***models*** (**articles/models.py**)
    1. ```date```
        - change *Timezone* (i.e. ```UTC``` => ```America/New_York```) in **settings.py**
    2. ```author```
        - we're using the one which we've created before 
            - specifically: ```users.CustomUser``` (set as ```AUTH_USER_MODEL)
        - we can do this via ```get_user_model``` 
    3. ```title```
    4. ```body```
- let's make some *migrations* & *register* work
    - migrate
        1. ```./manage.py makemigrations``` **```articles```**
        2. ```./manage.py migrate```
    - register (**articles/admin.py**)
        - ```from .models import Article```<br>```admin.site.register(Article)``` 
- okay! Now we can run the server to check what've done! 
    - go directly to URL/**admin**, just in case you forgot
- btw, if u mistyped some cols in the ```models.py```
    - just migrate again then it's fine 
    - **make** and **migrate** (btw, the arg of 1st step should be the same u've typed before)

### Let's setup the **URLs** & **Views**
- the steps we did before (just take this as a reminder!)
    1. add app & let django knows it 
    2. write models & make migrations 
    3. register at admin
- let's start (writing order, may not correlate to the exec order)
    1. add proj-level app-url (i.e. URL/articles/XXX)
    2. add *missing* app-level url 
        - add *missing* app-related views 
            - add *missing* view-related templates 
    3. okay! let's go to URL/**articles**/ to check the result! 

### What do we got for now? 
- Well, there's only the basic 'urls' & 'views' have been finished 
    - we now can display the articles (beautified by 'Bootstrap', which is nice)
    - but still left the "**Edit**" & "**Delete**" unfinished
    - Let's starting to implement that! 
- Ah. about the app: **articles**
    - let's do these: urls => view => each its templates 
- Impl details (sort of)
    - what to add 
        1. R U D -> (Read, Update, Delete) 
        2. Detail
    - a word about *specifically*
        1. R means 'Article List'
        2. Detail means '(specific) Article Detail'
- Ah! Let's finished the ***C*** (create) part! (of **CRUD**)
    - base 
        1. views: ```ArticleCreateView```
        2. urls: ```path(...)```
        3. templates
    - note 
        - I've put the 'create' part before any parts of the code,
        - just want to corrospond the 'CRUD' (ordering) :P

### Ok! the basic 'CRUD' part was done! 
- Now let's add the ```article_new``` to the navbar of homepage! 
    - file to change: **base.html**
    - any logic here: *whether the user is logged in or not*
- Let's beautifying the homepage (again)! 
    - file to change: **home.html**
    - wut being used: **Bootstrap**

### Alright! Let's talk about some DB-related crap! 
- Check the URL addr while ur editing
    - if there's 3 articles, 
        - u del one, then added one. 
        - **the URL of the new one** will continue the index (in cmp to total num of posts)
    - 0, 1, 2 
        - del 1, add -> 3 
        - the 2 won't take the '1's place
    - to be clear 
        - the index continues 
        - the content has gone, for good
    - in real world (quotes)
        1. most of them don't actually del anything 
        2. instead, they 'hide' delete fields which 
            - easier to main the integrity of a database 
            - give the option to "undelete" later (if needed)


# Chapter 14 (still based on Chapter 08) 

### Now, let's start fixing the biggest problems exists for a long time 
- which is 
    - **everyone** can edit/del anything on the website (well, actually NOT that)
    - if they know the URL (which is easy af, right?), let's **FIX IT**!

### Some concepts should be clear to u
- *authorization* & *authentication*
    1. the former: **restricts access** (e.g. all articles)
    2. the latter: **enables a user signup/login** flow 
- yep, Django is also has a built-in functionality for this 😊

### Fixes 
- no redudant author option when writing post<br>&nbsp;&nbsp;&nbsp;&nbsp;=> update the code of  ```ArticleCreateView``` (**views.py**)

### Introducing a new concept: ***Mixin***
- Why => "avoid" duplicate (code) yet still allow customization :P
- How => well, one step at a time! 

### Exactly ***how*** (& ***solving issues*** we've encoutered before)
- 0x00 
    1. The doc is ***awesome***! (Along with *Dash*)
- 0x01 
    - Problem
        - any user (even an anonymous one) could access the edit page 
        - well, you still can not submit the content (but still bad!)
    - Goals 
        - let's directly *forbidden* the anonymous user to access it 
    - Code    
        - articles/**views.py** 
            - ```from django.contrib.auth.mixins import LoginRequiredMixin```
            - ```class ArticleCreateView(LoginRequiredMixin, CreateView)```
        - articles/**views.py** 
            - inside the ```ArticleCreateView```
                - add ```login_url = 'login'```
    - Result 
        - The 'edit' page now can't be accesed for those not-logged-in user
        - But you'll encounter a '404' Page :) 
            - ya need add the ```login_url``` to name a url for redirecting purpose
            - it'll redirect to the page  u named 
                - when the user is not logged in, which makes more senses :) 
- 0x02 
    - Problem
        - *Nothing new* (**still based on 0x01**)
    - Goals 
        - Not allowing any not-logged-in user to do any of the CRUD opts. 
    - Code 
        - Still 
            - articles/**views.py**
            - from blabla import LoginRequiredMixin
        - The only difference is to change the *classname* & *redirect-url*
            - ```Article[XXX]View(LoginRequiredMixin, XXXView):```
            - ...... ```model = Article``` ......
            - ```login_url = "login"```
    - Result 
        - If you're not logged in, you won't be able to do the CRUD opts.
- 0x03 
    - Problem 
        - The not-logged-in permission has been restricted to minimum.
        - **Yet still**, the user that already logged in 
            - ***could make changes to any articles*** (which is **NOT** normal & not good in real word cases) 
            - 
    - Goals 
        - In a simplest solution, which is,
            - **only the author could make changes** to his/her posts - makes senses, huh?
    - Code
        - Base 
            - FILE: articles/**views.py**
            - IMPORT: ```from django.core.exceptions import PermissionDenied```
        - Changes 
            - CLASS
                - ```ArticleUpdateView```
                - ```ArticleDeleteView```
            - METHOD 
                - rewrite the ```dispatch()``` (go see the code!)
    - Result 
        - The posts can only be edit/del by its author, 
        - other than that? nope :P (which accomplished the task!)


# Chapter 15 (still based on Chapter 08) 

### Goals 
- Add a dedicated ```comments``` app and link it to ```articles```

### Steps 
- basis 
    - what to add 
        - FILE: articles/**models.py**
        - CLASS: ```Comment(models.Model)``` (newly added)
    - and 
        - ```./manage.py makemigrations articles```
        - ```./manage.py migrate```
    