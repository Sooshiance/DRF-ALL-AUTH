from rest_framework import decorators, response


@decorators.api_view(['GET'])
def home(request):
    return response.Response(request.data)
