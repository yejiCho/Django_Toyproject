# from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # http://127.0.0.1:8000/fcuser/register/
    path('register/', views.register),
    path('login/',views.login),
    # path('admin/', admin.site.urls),
    # path('fcuser/', include('fcuser.urls'))
]