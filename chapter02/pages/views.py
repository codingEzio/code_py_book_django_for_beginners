from django.http import HttpResponse

# Create your views here.


def Homepage(request):
    return HttpResponse("Hey django")
