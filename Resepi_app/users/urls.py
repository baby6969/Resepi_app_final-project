from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ProfileViews


urlpatterns= [
 path('register/',RegisterView.as_view() , name = 'register' ),
 path ('login/', obtain_auth_token , name='login'),
 path ('me/', ProfileViews.as_view() ,name = 'profile'),
]