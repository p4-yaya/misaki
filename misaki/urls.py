from django.urls import path
from . import views

app_name = "misaki"

urlpatterns = [
    path("", views.tela1, name="login"),
    path("tela2/", views.tela2, name="inicial"),
    path("tela3/", views.tela3, name="produtos"),
]