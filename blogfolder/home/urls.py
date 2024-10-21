from django.urls import path

from .views import HompageView
# from .views import add_user
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HompageView.as_view(), name='homepage'),
    path('add-user/', views.add_user, name='add_user'),
    path('', views.HompageView.as_view(), name='home'),
       # URL pattern named 'home'
    # path('user-list/', views.user_list, name='user_list'),
       # Ensure this line is included
]




