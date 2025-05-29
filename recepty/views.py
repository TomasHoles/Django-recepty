from django.shortcuts import render, get_object_or_404
from .models import Recept, Kategorie, Kuchar
from django.views.decorators.http import require_http_methods

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
