from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve as static_serve
from bio.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

# Serve static files through Django on Vercel (no web server available)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^static/(?P<path>.*)$', static_serve, {'insecure': True})]
