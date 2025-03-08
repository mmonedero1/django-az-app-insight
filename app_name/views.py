from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import logging
# from azure.monitor.opentelemetry import configure_azure_monitor
# configure_azure_monitor(logger_name='myapp')
logger = logging.getLogger('myapp')
logger.setLevel(logging.INFO)

@api_view(['GET'])
def echo_params(request):
    logger.info("*---> *******echo")
    return Response("conexión realizada", status=status.HTTP_200_OK)