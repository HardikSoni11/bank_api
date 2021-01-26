from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('api/branches/autocomplete/', views.branchDetail, name="branchDetail"),
    path('api/branches/', views.searchAllDetails, name="searchAllDetail"),
]
