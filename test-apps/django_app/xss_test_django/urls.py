from django.contrib import admin
from django.urls import path
from vulnerable_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vulnerable/', views.vulnerable_view1),
    path('safe/', views.safe_view),
]