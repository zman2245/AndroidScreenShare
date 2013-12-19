from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import tempfile
import shutil
from lockfile import FileLock

FILE_UPLOAD_DIR = '/Users/zfoster/code/django/android_screen_share/android_screen_share/media/test.png'

@csrf_exempt
def setscreen(request):
    with FileLock(FILE_UPLOAD_DIR):
        with open(FILE_UPLOAD_DIR, 'wb') as f:
            f.write(request.body)
            f.close()
    
    #with open(FILE_UPLOAD_DIR, 'wb') as dest:
    #    shutil.copyfileobj(request.FILES['filedata'], dest)
    return HttpResponse("hello world. screen share: " + str(len(request.FILES))) 

def getscreen(request):
    return render(request, 'android_screen_share/getscreen.html')

def getimage(request):
    with FileLock(FILE_UPLOAD_DIR):
        with open(FILE_UPLOAD_DIR, 'rb') as f:
            data = f.read()
            return HttpResponse(data, mimetype='image/png')

def setclick(request):
    xPercent = request.POST['xPercent']
    yPercent = request.POST['yPercent']


