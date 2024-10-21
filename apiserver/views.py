from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def index(request):
    data = {"result":"success","Data":[{"id":"itstudy","name":"Adam"}]}
    return Response(data, status=status.HTTP_200_OK)

