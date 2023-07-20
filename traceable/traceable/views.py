from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'register': reverse('user-register', request=request, format=format),
        'login': reverse('user-login', request=request, format=format),
        'logout': reverse('user-logout', request=request, format=format),
        'fetch-users': reverse('fetch-users', request=request, format=format),
    })