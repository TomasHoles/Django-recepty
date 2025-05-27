from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.seznam_receptu, name='seznam_receptu'),
    path('recept/<int:pk>/', views.detail_receptu, name='detail_receptu'),
    # Cesty pro jednotlivé kategorie
    path('hlavni-jidla/', views.kategorie_recepty, {'kategorie_nazev': 'Hlavní jídla'}, name='hlavni_jidla'),
    path('polevky/', views.kategorie_recepty, {'kategorie_nazev': 'Polévky'}, name='polevky'),
    path('dezerty/', views.kategorie_recepty, {'kategorie_nazev': 'Dezerty'}, name='dezerty'),
    # Cesta pro stránku s výběrem ingrediencí
    path('ingredience/', views.ingredience_vyber, name='ingredience_vyber'),
    # Stránka se seznamem autorů
    path('autori/', views.seznam_autoru, name='seznam_autoru'),
    # Stránka s detaily autora a jeho recepty
    path('autor/<int:autor_id>/', views.detail_autora, name='detail_autora'),
]

