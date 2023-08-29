from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from ITI_Store import settings
from .views import user, git_user_info, update_user_info, user_login, user_signup

urlpatterns = [
    path('img/<int:imgId>', user),
    path('api/git_user_info/<int:user_id>', git_user_info, name='get-user-info'),
    path('api/update_user_info/<int:user_id>', update_user_info, name='update-user-info'),
    path('api/login/', user_login, name='user-login'),
    path('api/signup/', user_signup, name='user-signup'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
