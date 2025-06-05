from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
import json
from .models import Recept, Kategorie, Kuchar

def seznam_receptu(request):
    """Zobrazí hlavní stránku se seznamem všech receptů."""
    recepty = Recept.objects.all()
    return render(request, 'recepty/seznam_receptu.html', {'recepty': recepty})

def detail_receptu(request, pk):
    """Zobrazí detail konkrétního receptu včetně ingrediencí a postupu.
    
    Args:
        pk: ID receptu v databázi
    """
    recept = get_object_or_404(Recept, pk=pk)
    return render(request, 'recepty/detail_receptu.html', {'recept': recept})

def kategorie_recepty(request, kategorie_nazev):
    """Zobrazí recepty filtrované podle kategorie.
    
    Args:
        kategorie_nazev: Název kategorie pro filtrování
    """
    recepty = Recept.objects.filter(kategorie__nazev=kategorie_nazev)
    return render(request, 'recepty/seznam_receptu.html', {
        'recepty': recepty,
        'aktivni_kategorie': kategorie_nazev
    })

@require_http_methods(["GET", "POST"])
def ingredience_vyber(request):
    """Stránka pro výběr ingrediencí a filtrování receptů.
    
    GET: Zobrazí formulář pro výběr ingrediencí
    POST: Zobrazí recepty obsahující vybrané ingredience
    """
    # Získání všech dostupných ingrediencí
    vsechny_ingredience_set = set()
    for recept in Recept.objects.all():
        try:
            ingredience = [ing.strip() for ing in recept.ingredience_list]
            vsechny_ingredience_set.update(ingredience)
        except json.JSONDecodeError:
            continue

    vsechny_ingredience = sorted(vsechny_ingredience_set)
    vybrane_ingredience = request.POST.getlist('ingredience') if request.method == 'POST' else []
    recepty = []

    if vybrane_ingredience:
        # Filtrování receptů podle vybraných ingrediencí
        for recept in Recept.objects.all():
            try:
                recept_ingredience = [ing.strip() for ing in recept.ingredience_list]
                if any(ing in recept_ingredience for ing in vybrane_ingredience):
                    recepty.append(recept)
            except json.JSONDecodeError:
                continue

    return render(request, 'recepty/ingredience_vyber.html', {
        'vsechny_ingredience': vsechny_ingredience,
        'vybrane_ingredience': vybrane_ingredience,
        'recepty': recepty
    })

def seznam_autoru(request):
    """
    View pro zobrazení seznamu všech autorů.
    """
    autori = Kuchar.objects.all()
    return render(request, 'recepty/seznam_autoru.html', {'autori': autori})

def detail_autora(request, autor_id):
    """
    View pro zobrazení detailu autora a jeho receptů.
    """
    autor = get_object_or_404(Kuchar, pk=autor_id)
    recepty = Recept.objects.filter(kuchar=autor)
    return render(request, 'recepty/detail_autora.html', {'autor': autor, 'recepty': recepty})

@require_http_methods(["GET", "POST"])
def pridat_recept(request):
    """View pro přidání nového receptu."""
    if request.method == 'POST':
        nazev = request.POST.get('nazev')
        popis = request.POST.get('popis')
        kategorie_id = request.POST.get('kategorie')
        kuchar_id = request.POST.get('kuchar')
        ingredience = request.POST.getlist('ingredience[]')
        postup = request.POST.getlist('postup[]')
        obrazek = request.FILES.get('obrazek')

        try:
            kategorie = Kategorie.objects.get(id=kategorie_id)
            kuchar = Kuchar.objects.get(id=kuchar_id)
            
            recept = Recept.objects.create(
                nazev=nazev,
                popis=popis,
                kategorie=kategorie,
                kuchar=kuchar,
                obrazek=obrazek,
                ingredience=json.dumps(ingredience),
                postup=json.dumps(postup)
            )
            return redirect('detail_receptu', pk=recept.pk)
        except Exception as e:
            messages.error(request, f'Chyba při ukládání receptu: {str(e)}')
    
    kategorie = Kategorie.objects.all()
    kuchari = Kuchar.objects.all()
    return render(request, 'recepty/pridat_recept.html', {
        'kategorie': kategorie,
        'kuchari': kuchari
    })

@require_http_methods(["POST"])
def odebrat_recept(request, pk):
    """View pro odebrání receptu."""
    recept = get_object_or_404(Recept, pk=pk)
    recept.delete()
    return redirect('seznam_receptu')
