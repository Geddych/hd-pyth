"""hd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from hdesk import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',views.index,name='index'),
    path(r'technic/',views.technic,name = 'technic'),
    path(r'add_rec/',views.add_record,name='add_record'),
    path(r'rec/<id>',views.edit_rec,name = 'edit_record'),
    path(r'add_tec/',views.add_tec, name = 'add_tec'),
    path(r'add_dep/',views.add_dep, name = 'add_dep'),
    path(r'send/<id>',views.send_tec, name = 'send'),
    path(r'conf/<id>',views.confirm_tec, name = 'confirm'),
    path(r'writeoff/<id>',views.writeoff,name = 'writeoff'),
    path(r'return/<id>',views.return_tec, name = 'return'),

]
