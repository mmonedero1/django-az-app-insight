import logging
import json

logger = logging.getLogger('django')

class LogRequestResponseBodyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the request body
        if request.content_type == 'application/json':
            try:
                request_data = json.loads(request.body)
                pretty_request = json.dumps(request_data, indent=4, sort_keys=True, ensure_ascii=False)
                logger.info(f"*--Sr-< {request.path} - {request.method} - {pretty_request}")
            except json.JSONDecodeError:
                logger.info(f"*--Sr-< {request.path} - {request.method} - {request.body}")
        else:
            if not isinstance(request.body, (bytes, bytearray)):
                logger.info(f"*--Sr-< {request.path} - {request.method} - {request.body}")

        response = self.get_response(request)

        # Log the response body
        if hasattr(response, 'content') and ('Content-Type' in response) and (response['Content-Type'] == 'application/json'):
            try:
                response_data = json.loads(response.content)
                pretty_response = json.dumps(response_data, indent=4, sort_keys=True, ensure_ascii=False)
                logger.info(f"*--Sr-> {request.path} - {request.method} - {pretty_response}")
            except json.JSONDecodeError:
                logger.info(f"*--Sr-> {request.path} - {request.method} - {response.content}")
        else:
            if not isinstance(response.content, (bytes, bytearray)):
                logger.info(f"*--Sr-> {request.path} - {request.method} - {response.content}")

        return response