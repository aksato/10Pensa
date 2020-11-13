from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
]