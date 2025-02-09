from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.renderers import TemplateHTMLRenderer


@api_view(['GET', 'POST'])
def first_view(request):
    if request.method == 'GET':
        return Response({'message': 'Hello World!'}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            msg = request.data['message']
            return Response({'your_message': msg}, status=status.HTTP_201_CREATED)
        except:
            return Response({'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)
