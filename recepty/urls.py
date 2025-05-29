from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Definice URL adres a jejich mapování na views
urlpatterns = [
    # Hlavní stránka se seznamem všech receptů
    path('', views.seznam_receptu, name='seznam_receptu'),
    
    # Detail konkrétního receptu (používá ID receptu)
    path('recept/<int:pk>/', views.detail_receptu, name='detail_receptu'),
    
    # URL pro jednotlivé kategorie
    path('hlavni-jidla/', views.kategorie_recepty, {'kategorie_nazev': 'Hlavní jídla'}, name='hlavni_jidla'),
    path('polevky/', views.kategorie_recepty, {'kategorie_nazev': 'Polévky'}, name='polevky'),
    path('dezerty/', views.kategorie_recepty, {'kategorie_nazev': 'Dezerty'}, name='dezerty'),
    
    # Stránka pro výběr ingrediencí
    path('ingredience/', views.ingredience_vyber, name='ingredience_vyber'),
    
    # Stránky pro autory
    path('autori/', views.seznam_autoru, name='seznam_autoru'),
    path('autor/<int:autor_id>/', views.detail_autora, name='detail_autora'),
]

