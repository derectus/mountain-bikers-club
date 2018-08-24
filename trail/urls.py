from django.urls import path

from . import views


urlpatterns = [
    path('new/', views.upload, name='upload'),
    path('<uuid:trail_id>/edit/', views.edit, name='trail__edit'),
    path('<uuid:trail_id>/delete/', views.delete, name='trail__delete'),
    path('<uuid:trail_id>/', views.view, name='trail'),
]
