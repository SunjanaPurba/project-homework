
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_F/', include('app_F.urls')),
    
    path('studentcoverpage/', include('studentcoverpage.urls'))
]
