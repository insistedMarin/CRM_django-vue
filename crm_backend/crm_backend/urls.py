"""
URL configuration for crm_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from crm_app.views import register_api, LoginView, get_user_info, send_verification_code, CustomerViewSet, SalesOpportunityViewSet


router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'salesopportunities', SalesOpportunityViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', register_api, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user_info/', get_user_info, name='user_info'),
    path("send_verification_code/", send_verification_code, name="send_verification_code"),

    # 添加这行来包含我们的DRF URLs
    path('', include(router.urls)),
]
