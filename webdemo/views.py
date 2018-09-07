from django.http import HttpResponse
import datetime


def hello(request):
    now = datetime.datetime.now()
    return HttpResponse("<h1>%s</h1>" % (now,))
