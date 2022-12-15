from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('newpage/',views.new_page,name="get_val"),
    path('loginform/',views.loginform,name="loginform"),
    path('account/',views.account,name="account"),
    path('request_access/$', views.request_access,name='request_access')
]
