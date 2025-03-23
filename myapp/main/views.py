from django.shortcuts import HttpResponse
from main.models import MyModel
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get(request):
    if request.method == 'GET':
        return HttpResponse(str(MyModel.objects.all().values()))
    return HttpResponse('')

@csrf_exempt
def post(request, text):
    if request.method == 'POST':
        MyModel.objects.create(textfield=text, intfield=len(text), boolfield=(len(text) % 2 == 0))
        return HttpResponse('OK')
    return HttpResponse('')


# Create your views here.
