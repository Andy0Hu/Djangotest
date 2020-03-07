# Create your views here.
from django.http import HttpResponse
import json
from predict import *

def index(request):
    if request.method == 'POST':
        json_result = json.loads(request.body.decode().replace("'", "\"")).get('name')
        val = predict(json_result)
        return HttpResponse(val)
    else:
        return HttpResponse("请求错误")
