from django.http import HttpResponse


def home(request):
    html = '<h1><marquee>Music Music</marquee></h1>'
    return HttpResponse("<h1><marquee>Music Music</marquee></h1>")