from django.urls import path, re_path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user, name='login_user'),
    path('register_user/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('course/', include(('course.urls', 'course'), namespace='course')),
    path('instructor/', include(('instructor.urls', 'instructor'), namespace='instructor')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
