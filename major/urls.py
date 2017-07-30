"""major URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'stock.views.home', name='home1'),#home page
    url(r'^prediction/', 'stock.views.prediction', name ='prediction'),#prediction
    url(r'^data/$', 'stock.views.data', name ='show_data'),
    url(r'^analysis/$', 'stock.views.analysis', name ='analysis'),#analysis
    url(r'^about/$', 'stock.views.about', name ='about'),#about
    url(r'^updatedata/$', 'stock.views.update_data', name ='update_data'),#update data
    url(r'^updatedatadaily/$', 'stock.views.update_data_daily', name ='update_data_daily'),#live data    
]
