from rest_framework.response import Response
from rest_framework import status

def candidate_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role != 'candidate':
            return Response(
                {"error": "Candidate access only"},
                status=status.HTTP_403_FORBIDDEN
            )
        return view_func(request, *args, **kwargs)
    return wrapper
