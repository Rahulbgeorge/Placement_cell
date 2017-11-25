"""placement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from . import views
from . import views2
urlpatterns = [
    url(r'^$',views.home,name="home_page"),
    url(r'^login/$',views.login_page,name="login_page"),
    url(r'^upload/$',views.upload_file),
    url(r'^logout/$',views.logout_page),
    url(r"^projects/$",views2.project_view),

]
