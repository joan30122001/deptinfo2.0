from django.contrib import admin
from django.urls import path, include, re_path
from barbillard.views import home

from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('admin/', admin.site.urls),
    path('barbillard/', include("barbillard.urls")),
    path('blog/', include("blog.urls")),
    path('enseignement/', include("enseignement.urls")),
    path('', home, name='home'),
    
    path('i18n/', include('django.conf.urls.i18n')),
    path('rosetta/', include('rosetta.urls')),
    
    re_path(r'^maintenance-mode/', include('maintenance_mode.urls')), # Django maintenance mode
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = _('Département d\'Informatique')
admin.site.index_title = _("Zone d\'Administration")
admin.site.site_title = _('Département d\'Informatique')
