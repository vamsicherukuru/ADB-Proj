from django.urls import path
from ChristKart import views

app_name = 'ChristKart'

urlpatterns=[
path('plates',views.plates.as_view(),name='plates'),
path('straws',views.straws.as_view(),name='straws'),
path('bags',views.bags.as_view(),name='bags'),

]
