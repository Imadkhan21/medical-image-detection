"""medical_classification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("disease_detection.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('disease_detection.urls')),  # Your app name
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# FYP/urls.py
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('', include('disease_detection.urls')),  # your app's URLs
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# urls.py
from django.urls import path
from disease_detection.views import kidney_disease_detect

from disease_detection.views import home, kidney_disease_detect 


from django.urls import path
from disease_detection import views  # Replace with the correct app name


urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.info, name='info'),  # Make sure this exists
    path('detect/', views.kidney_disease_detect, name='kidney_disease_detect'),
]


# urlpatterns = [
#     path('', home, name='home'),  # this handles the root URL
#     path('detect/', kidney_disease_detect, name='kidney_disease_detect'),

# ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
