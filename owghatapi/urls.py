from django.urls import path
from . import views

urlpatterns = [
    path('<str:long>/<str:lat>', views.lat_long),
    path('<str:city>/', views.city),
    path('<int:year>/<int:month>/<int:day>/<str:lat>/<str:long>/<str:tz>/', views.date_lat_long)
]
