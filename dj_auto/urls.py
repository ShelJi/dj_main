from django.urls import path
from . import views


app_name = "dj_auto"

urlpatterns = [
    path("import-data/", views.ImportData.as_view(), name="import_data"),
]
