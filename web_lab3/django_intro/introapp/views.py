from json import loads

from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from introapp.models import CalculateResponse, CalculateRequest
from introapp.serrializers import CalculationResponseSerializer, CalculationRequestSerializer
from introapp.Calculation import Calculator

"""
Клас, що описує точку доступа до API застосунку. Має наслідуватись від
APIView.
"""


class ExampleView(APIView):

    def post(self, request: HttpRequest):
        """
        Описує обробник POST запитів для даної точки доступу. Аналогічно можна визначити
        обробники і для інших HTTP методів.
        """
        parsed_request = loads(request.body)
        request_data_serializer = CalculationRequestSerializer(data=parsed_request)
        if not request_data_serializer.is_valid():
            return Response(status=400)
        request_data = CalculateRequest(**request_data_serializer.validated_data)
        calculation_result = Calculator.calculate(request_data.input_value)
        response_data = CalculateResponse(calculation_result)
        response_data_serializer = CalculationResponseSerializer(response_data)
        response = Response(response_data_serializer.data)
        return response


from django.shortcuts import render

# Create your views here.
