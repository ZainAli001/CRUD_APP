from django.contrib import admin
from django.urls import path, include
# from home.views import index, home1, edit

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name="index"),
    path('', include("home.urls")),

]
