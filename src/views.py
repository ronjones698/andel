from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from estimator import estimator
from periodtype import data

class Estimates(APIView):
    def get(self,request,*args,**kwargs):
        Response({'data':'Hello'})
    def post():
        x = estimator(data)
        return Response(x)
        
