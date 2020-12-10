from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def get_sampple(request):
    sample_data = {
        "name": "toan",
        "age": 24,
        "gender": "male"
    }
    return Response(sample_data)