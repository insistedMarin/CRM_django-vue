from django.core.cache import cache
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from crm_app.forms import RegisterForm


@api_view(['POST'])
@permission_classes([AllowAny])
def register_api(request):
    verification_code = request.data.get('verification_code')
    email = request.data.get('email')

    if not verification_code or not cache.get(email) == verification_code:
        return Response({"detail": "Invalid verification code."}, status=status.HTTP_400_BAD_REQUEST)

    form = RegisterForm(request.data)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
