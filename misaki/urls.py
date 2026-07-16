from django.urls import path
from . import views

app_name = "misaki"

urlpatterns = [
    path("", views.inicial, name="inicial"),
    path("login/", views.login, name="login"),
    path("sobre/", views.sobre, name="sobre"),
    path("produtos/", views.produtos, name="produtos"),
]