"""djangoViewTemplates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from authentication.urls import router as user_api_router
from order.urls import router as order_api_router
from order.views import DoesOrderBelongsToUserAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    path('author/', include('author.urls')),
    path('auth/', include('authentication.urls')),
    path('order/', include('order.urls')),
    path('api/v1/users/', include(user_api_router.urls)),
    path('api/v1/users/<int:user_id>/order/<int:order_id>/', DoesOrderBelongsToUserAPIView.as_view()),
    path('api/v1/orders/', include(order_api_router.urls)),
]
