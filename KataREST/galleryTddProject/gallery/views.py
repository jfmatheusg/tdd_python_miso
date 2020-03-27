from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Image
import json


# Create your views here.
@csrf_exempt
def index(request):
    image_list = []
    return HttpResponse(serializers.serialize('json', image_list))