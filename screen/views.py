from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from django.views import generic

from screen.models import Screen

@csrf_exempt
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
