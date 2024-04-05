from django.urls import path
from . import views

urlpatterns = [
    path("trabalhe-conosco/", views.TrabalheConoscoView.as_view(), name="trabalheConosco"),
    path("sobre-nos/", views.SobreNosView.as_view(), name="sobreNos")

]
