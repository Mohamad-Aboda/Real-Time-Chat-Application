from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),

]
