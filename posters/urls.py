from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posters, name='posters'),
    path('<int:poster_id>/', views.poster_info, name='poster_info'),
    path('add/', views.add_poster, name='add_poster'),
    path('edit/<int:poster_id>/', views.edit_poster, name='edit_poster'),
    path('delete/<int:poster_id>/', views.delete_poster, name='delete_poster'),
]
