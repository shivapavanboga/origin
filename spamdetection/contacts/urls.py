from django.urls import path
from .views import SearchByName,SearchByPhone

urlpatterns = [
    path('search/name/',SearchByName.as_view() , name='search_by_name'),
    path('search/phone/', SearchByPhone.as_view(), name='search_by_phone'),
]
