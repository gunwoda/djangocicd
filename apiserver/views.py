from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def index(request):
    data = {"result1":"success1","Data1":[{"id":"itstudy1","name":"Adam1"}]}
    return Response(data, status=status.HTTP_200_OK)

