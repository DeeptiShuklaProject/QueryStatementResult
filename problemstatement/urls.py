"""
URL configuration for problemstatement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from myapp.views import ProblemStatementViewSet, TagViewSet
# from myapp.views import export_csv
# from myapp.views import download_csv

# # Define the router
# router = DefaultRouter()
# router.register(r'problem-statements', ProblemStatementViewSet)
# router.register(r'tags', TagViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('export-csv/', export_csv, name='export_csv'),
#     path('download-csv/', download_csv, name='download_csv'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import ProblemStatementViewSet, TagViewSet, MasterDataViewSet
from myapp.views import export_csv, download_csv
from myapp.views import MasterDataViewSet

# Define the router
router = DefaultRouter()
router.register(r'problem-statements', ProblemStatementViewSet)
router.register(r'tags', TagViewSet)
router.register(r'master-data', MasterDataViewSet)  # Register MasterDataViewSet

urlpatterns = [
    # Include the registered routes
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    
    # Additional custom views
    path('export-csv/', export_csv, name='export_csv'),
    path('download-csv/', download_csv, name='download_csv'),
]









