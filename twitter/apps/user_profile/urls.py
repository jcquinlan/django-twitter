from django.conf.urls import url
from . import views

urlpatterns = [
    # Registration URLS
    url(r'^register/$', views.register, name='register'),
    url(r'^register/process/$', views.register_process, name='register_process'),
    url(r'^register/success/$', views.register_success, name='register_success'),

    # Sign In URLS
    url(r'^sign-in/$', views.sign_in, name='sign_in'),
    url(r'^sign-in/process/$', views.sign_in_process, name='sign_in_process'),

    # Sign Out URL
    url(r'^sign-out/$', views.sign_out, name='sign_out'),

]
