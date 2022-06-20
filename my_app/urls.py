from django.urls import path, include
from django.contrib import admin
from . import views
from django.views.generic.base import TemplateView
urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path("cars/", views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-car'),
    path('cars/update/<int:car_id>', views.update_car),
    path('cars/delete/<int:car_id>', views.delete_car)
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
]