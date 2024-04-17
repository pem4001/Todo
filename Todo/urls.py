"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import home,create,edit,delete,delete_all_datas    # Here, "home" and "create" function is called from base/view location

urlpatterns = [
    path('admin/', admin.site.urls),  #This url iwll call "Admin" panel
    path('',home, name="home88"),  # name="home88" runs inside project;
    path('create/',create, name="create88"),   #create in 2nd paramaeter will lead to "create" function in "views.py"
    path('edit/<int:pk>/',edit, name="edit88"),
    path('delete/<int:pk>/',delete, name="delete88"),
    path('delete_all/',delete_all_datas, name="delete_all_datas88")
    
]
 