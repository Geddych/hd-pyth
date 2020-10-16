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
    path(r'technic/delete/<id>',views.del_tec),
    path(r'technic/edit/<id>',views.edit_tec),

    path(r'records',views.records),
    path(r'records/add',views.add_record,name='add_record'),
    path(r'records/edit/<id>',views.edit_rec,name = 'edit_record'),
    path(r'records/send/<id>',views.send_tec, name = 'send'),
    path(r'records/get/<id>',views.confirm_tec, name = 'confirm'),
    path(r'records/return/<id>',views.return_tec, name = 'return'),
    path(r'records/writeoff/<id>',views.writeoff,name = 'writeoff'),

    path(r'departments/',views.depart),
    
    path(r'logout/',views.user_logout),
    path(r'exc/',views.download_a_csv)

]
