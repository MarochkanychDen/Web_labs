from json import dumps, loads
import logging
import redis

from rest_framework.views import APIView
from django.http import HttpRequest
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import SerializerData
from .models import teams


logger = logging.getLogger('django')
redis_access = redis.Redis('localhost', port=6379, db=15)


class teamView(APIView):

    def __init__(self):
        super().__init__()
        self.serializer = SerializerData
        self.teamlIST = teams.objects.all()

    # отримання даних(якщо немає id вибираємо всі записи)
    def get(self, request: Request):
        id = request.query_params.get('id', None)
        if id is None:
            teamlIST = self.teamlIST.all()
            serializer = self.serializer(teamlIST, many=True)
            return Response(serializer.data)
        else:
            return self.get_details(id)

    # оновлюємо запис по id
    def post(self, request: HttpRequest):
        body = loads(request.body)
        serializer = self.serializer(data=body)
        if not serializer.is_valid():
            return Response(status=400)
        model = teams(**serializer.data)
        model.pk = serializer.data['id']
        model.save()

        redis_access.delete(model.pk)
        return Response(status=200)


    # сворюємо запис
    def put(self, request: HttpRequest):
        body = loads(request.body)
        serializer = self.serializer(data=body)
        if not serializer.is_valid():
            return Response(status=400)

        teams(**serializer.data).save()

        return Response(status=201)
     # видаляємо запис
    def delete(self, request: HttpRequest):
        body = loads(request.body)
        id = body['id']
        self.teamlIST.get(id=id).delete()
        redis_access.delete(id)

        return Response(status=200)

    # отримання запису по id
    def get_details(self, pk: int):
        logger.info(f'getting record with id={pk}')
        cached = redis_access.get(pk)
        if cached:
            logger.info(f'got record with id={pk} from redis')
            return Response(loads(cached))

        logger.info(f"had to query record with id={pk} from db")
        try:
            obj = self.teamlIST.get(id=pk)
        except:
            return Response(status=400)
        serializer = self.serializer(obj)
        data = serializer.data
        redis_access.set(pk, dumps(data))
        return Response(data)