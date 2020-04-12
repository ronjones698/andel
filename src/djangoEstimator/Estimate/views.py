from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from estimator import estimator
from django.http import JsonResponse,HttpResponse
#from periodtype import data
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from dicttoxml import dicttoxml
from src.estimator import estimator

@api_view(['GET','POST'])
def xmlresponse(request):
    if request.method == 'POST':
        data =JSONParser().parse(request)
        x = estimator(data)
        y = dicttoxml(x)
        return HttpResponse(y,content_type = 'text/xml')


class Estimates(APIView):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        x = estimator(data)
        return Response(x)