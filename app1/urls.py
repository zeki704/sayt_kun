from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name="home"),
    path("contact/", cnt, name="contact"),
    path("ctg/<int:_id>/", ctg, name="ctg"),
    path("view/<int:pk>", view, name="view"),
    path("search/", srch, name="search"),
    # path("all/", alljson, name="all"),
]