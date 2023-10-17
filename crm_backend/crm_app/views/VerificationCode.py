from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.cache import cache
import random

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([AllowAny])
def send_verification_code(request):
    email = request.data.get('email')
    # Check if email is already in use
    if User.objects.filter(email=email).exists():
        return Response({"detail": "Email already in use."}, status=status.HTTP_400_BAD_REQUEST)

    verification_code = str(random.randint(100000, 999999))

    # Store in cache for 10 minutes
    cache.set(email, verification_code, 600)

    # Send email
    send_mail(
        'Your verification code',
        f'Your verification code is: {verification_code}',
        'from_email@example.com',
        [email],
        fail_silently=False,
    )

    return Response({"message": "Verification code sent."})
