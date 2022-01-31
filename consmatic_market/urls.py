from django.contrib import admin
from django.urls import path, include
from makeup import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index.html'),
    path('makeup/', include("makeup.urls"))
]
