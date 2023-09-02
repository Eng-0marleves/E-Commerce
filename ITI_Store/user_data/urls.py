from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from ITI_Store import settings
from .views import *

urlpatterns = [
    path('', signupPage, name='signup-page'),
    path('login/', loginPage, name='login-page'),

    path('img/<int:imgId>', user_image),
    path('api/get_user_info/<int:user_id>', get_user_by_id, name='get-user-info'),
    path('api/get_user/', get_user_by_email, name='get-user'),
    path('api/update_user_info/<int:user_id>', update_user_info, name='update-user-info'),
    path('api/signup/', user_signup, name='user-signup'),


    path('', SignupView.as_view(), name='view-signup'),
    path('api/signup/', SignupAPIView.as_view(), name='api-signup'),
    path('login/', LoginView.as_view(), name='login-page'),
    path('api/login/', LoginAPIView.as_view(), name='api-login'),
    path('home/', homePage, name='home-page'),
    path('home/profile', profilePage, name='profile-page'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
