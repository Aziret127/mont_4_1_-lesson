from django.urls import path
from . import views
app_name='yaziki'
urlpatterns = [
    path('prog_lang/', views.ProgLangListView.as_view(), name='yaizki_programmirovanie'),
    path('prog_lang/<int:id>/', views.ProgLangDetailView.as_view(),),
    path('prog_lang/<int:id>/delete/', views.DeleteProglangView.as_view()),
    path('prog_lang/<int:id>/update/', views.UpdateProglangView.as_view()),

    path("create_prog_lang/", views.CreateProgLangView.as_view(), name='sozdat_blog'),
    path("search/", views.SeachView.as_view()),
]