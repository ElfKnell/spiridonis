"""spiridonis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    # path to djoser end points
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    # path to our account's app endpoints
    path('api/v1/accounts/', include('accounts.urls')),

    path('api/v1/users/', include('users.urls')),
    path('api/v1/category/', include('category.urls')),
    path('api/v1/product/', include('product.urls')),
    path('api/v1/manufacturer/', include('manufacturer.urls')),
    path('api/v1/attributes/', include('attibutes.urls')),
    path('api/v1/vproduct/', include('vproduct.urls')),
    path('api/v1/promotions/', include('promotions.urls')),
    path('api/v1/set/', include('set.urls')),
    path('api/v1/reviews/', include('reviews.urls')),
    path('api/v1/rating/', include('rating.urls')),
    path('api/v1/company/', include('company.urls')),
    path('api/v1/news/', include('news.urls'))
]
