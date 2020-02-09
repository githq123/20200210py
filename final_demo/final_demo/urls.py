"""final_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from apps.users import views
# from apps.cms.urls import router
# from apps.users import urls
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.RegisterView.as_view(),name='register'),
    path('index/', views.index,name='index'),
    path('admin/', views.admin,name='admin'),
    url(r'^user/', include('apps.users.urls', namespace='users')),
    url(r'^blog/', include('apps.blogs.urls', namespace='blogs')),
    path('password_reset/', include('password_reset.urls')),
    url(r'cms/',include('apps.cms.urls',namespace='cms')),
    url('^pachong/',include('apps.pachong.urls',namespace='pachong'))

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
