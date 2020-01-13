from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',include('core.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),


    ]
