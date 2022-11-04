from django.urls import path
from . import views

urlpatterns = [
    path("",views.ListArtisteAPIView.as_view(),name="artiste_list"),
    path("create/", views.CreateArtisteAPIView.as_view(),name="artiste_create"),
    path("update/<int:pk>/",views.UpdateArtisteAPIView.as_view(),name="update_artiste"),
    path("delete/<int:pk>/",views.DeleteArtisteAPIView.as_view(),name="delete_artiste")
]
