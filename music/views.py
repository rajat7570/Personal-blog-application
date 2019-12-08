from django.http import  HttpResponse

def index(request):
    return HttpResponse("<h1><B><I>I love music.</I></B></h1>")
