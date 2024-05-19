
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from condif.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path("", include("core.swagger.swagger")),  # swagger
    path("user/", include("apps.user.urls")),
    path("auth/", include("apps.auth.urls")),
    path("note/", include("apps.note.urls")),
    path("todo/", include("apps.todo.urls")),

]
urlpatterns += static(MEDIA_URL, document_root=settings.MEDIA_ROOT)
