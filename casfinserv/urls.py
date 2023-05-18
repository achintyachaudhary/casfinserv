from django.contrib import admin
from django.urls import path

from .views import BTSTAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BTSTAPIView, name='btst_view'),
]
