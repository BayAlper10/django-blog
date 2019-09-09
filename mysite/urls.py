
from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import login, logout
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
