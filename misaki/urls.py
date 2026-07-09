from django.urls import path
from . import views

app_name = "misaki"

urlpatterns = [
    path("", views.login, name="login"),
    path("inicial/", views.inicial, name="inicial"),
    path("produtos/", views.produtos, name="produtos"),
    path("produtos2/", views.produtos2, name="produtos2"),
    path("contato/", views.contato, name="contato"),
]