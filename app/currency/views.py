from django.http.response import HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse('Hello World!')
