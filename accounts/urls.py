from django.urls import path
from .views import user_login, register, profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('password_change/', auth_views.PasswordChangeView.as_view(),
        name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('password_reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
    path('profile/', profile, name='profile'),
]
