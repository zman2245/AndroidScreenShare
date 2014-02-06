from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from django.views import generic

from screen.models import Click, Screen

@csrf_exempt
def setclick(request):
    xPercent = request.POST['xPercent']
    yPercent = request.POST['yPercent']

    if Click.objects.filter(pk=1).count() == 0:
        click = Click()
    else:
        click = Click.objects.get(pk=1)

    click.xpercent = xPercent
    click.ypercent = yPercent
    click.is_valid = True

    click.save()

    data = simplejson.dumps({'success':'true'})
    return HttpResponse(data, mimetype="application/json")

def getclick(request):
    click = Click.objects.get(pk=1)
    if (click is None) or (not click.is_value):
        data = simplejson.dumps({'success':'false', 'reason':'no event available'})
        return HttpResponse(data, mimetype="application/json")

    data = simplejson.dumps({'success':'true', 'xpercent':click.xpercent, 'ypercent':click.ypercent})
    click.is_valud = False

    return HttpResponse(data, mimetype="application/json")

def newscreen(request):
    # TODO
    data = simplejson.dumps({'success':'true'})
    return HttpResponse(data, mimetype="application/json")

class SocketView(generic.TemplateView):
    template_name = "screen/socket.html"

class AllView(generic.ListView):
    template_name = "screen/all.html"
    context_object_name = "screens"

    def get_queryset(self):
        return Screen.objects.all()
