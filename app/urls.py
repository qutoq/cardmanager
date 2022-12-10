from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_view, name='main'),
    path('card/<int:id>', views.card_view, name='card'),
    path('card/<int:id>/status', views.status_change, name='status'),
    path('card/<int:id>/del', views.delete_view, name='delete'),
    path('search', views.search_view, name='search'),
    path('generate', views.generate_view, name='generate'),
]

app_name = 'app'
