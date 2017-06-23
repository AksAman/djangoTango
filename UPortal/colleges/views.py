from django.http import HttpResponse

from .models import College,Details


def index(request):
    content = '<h1><font color="red"><marquee>Welcome To the college homepage</marquee></font></h1><hr>'
    all_colleges=College.objects.all()
    for col in all_colleges:
        url = '/college/'+str(col.id)+'/'
        content += '<li><a href="'+url+'">'+col.college_name+'</a><br>'
    return HttpResponse(content)


def details(request, college_id):
    col = College.objects.filter(id=college_id)[0]
    html = '<h2>Details for College ID : '+college_id+'</h2><hr> '+col.college_name+'<br>'+col.state
    return HttpResponse(html)
