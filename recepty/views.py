from django.shortcuts import render, get_object_or_404
from .models import Recept, Kategorie, Kuchar
from django.views.decorators.http import require_http_methods

# Create your views here.

def seznam_receptu(request):
    recepty = Recept.objects.all()
    return render(request, 'recepty/seznam_receptu.html', {'recepty': recepty})

def detail_receptu(request, pk):
    recept = get_object_or_404(Recept, pk=pk)
    return render(request, 'recepty/detail_receptu.html', {'recept': recept})

def kategorie_recepty(request, kategorie_nazev):
    """
    View pro zobrazení receptů podle kategorie (Hlavní jídla, Polévky, Dezerty).
    """
    recepty = Recept.objects.filter(kategorie__nazev=kategorie_nazev)
    return render(request, 'recepty/seznam_receptu.html', {
        'recepty': recepty,
        'aktivni_kategorie': kategorie_nazev  # pro zvýraznění v menu
    })

# View pro stránku s výběrem ingrediencí a filtrováním receptů
@require_http_methods(["GET", "POST"])
def ingredience_vyber(request):
    """
    View pro výběr ingrediencí a zobrazení receptů, které lze z těchto ingrediencí uvařit.
    """
    # Sestavím množinu všech ingrediencí použitých v receptech
    vsechny_ingredience_set = set()
    for r in Recept.objects.all():
        if r.nazev == 'Svíčková na smetaně':
            ingred = ['hovězí svíčková', 'kořenová zelenina', 'cibule', 'slanina', 'smetana', 'ocet', 'cukr', 'bobkový list', 'nové koření', 'pepř', 'sůl', 'olej', 'máslo']
        elif r.nazev == 'Guláš':
            ingred = ['hovězí kližka', 'cibule', 'česnek', 'sladká paprika', 'majoránka', 'rajčatový protlak', 'sůl', 'pepř', 'sádlo']
        elif r.nazev == 'Česnečka':
            ingred = ['česnek', 'brambory', 'zeleninový vývar', 'majoránka', 'sůl', 'pepř', 'chleba', 'sýr']
        elif r.nazev == 'Kuřecí řízek':
            ingred = ['kuřecí prsa', 'hladká mouka', 'vejce', 'strouhanka', 'sůl', 'pepř', 'olej na smažení', 'bramborová kaše']
        elif r.nazev == 'Štrúdl':
            ingred = ['listové těsto', 'jablka', 'rozinky', 'skořice', 'cukr', 'vejce', 'vanilková zmrzlina']
        elif r.nazev == 'Rajská omáčka':
            ingred = ['hovězí maso', 'rajčata', 'cibule', 'mrkev', 'celer', 'petržel', 'bobkový list', 'nové koření', 'sůl', 'pepř', 'cukr', 'máslo', 'hladká mouka', 'citron', 'houskový knedlík']
        elif r.nazev == 'Bramboračka':
            ingred = ['brambory', 'houby', 'mrkev', 'celer', 'petržel', 'česnek', 'majoránka', 'sůl', 'pepř', 'máslo']
        elif r.nazev == 'Tiramisu':
            ingred = ['mascarpone', 'vejce', 'cukr', 'piškoty', 'káva', 'rum', 'kakao']
        elif r.nazev == 'Kuřecí kari':
            ingred = ['kuřecí prsa', 'kokosové mléko', 'kari koření', 'cibule', 'česnek', 'zázvor', 'rýže', 'olej', 'sůl', 'pepř']
        elif r.nazev == 'Čokoládový dort':
            ingred = ['čokoláda', 'máslo', 'vejce', 'cukr', 'hladká mouka', 'prášek do pečiva', 'mléko']
        elif r.nazev == 'Houbová polévka':
            ingred = ['houby', 'brambory', 'mrkev', 'celer', 'petržel', 'smetana', 'máslo', 'sůl', 'pepř']
        else:
            ingred = []
        vsechny_ingredience_set.update(ingred)
    vsechny_ingredience = sorted(vsechny_ingredience_set)
    vybrane_ingredience = request.POST.getlist('ingredience') if request.method == 'POST' else []
    recepty = []
    if vybrane_ingredience:
        # Filtrování receptů podle ingrediencí (pro ukázku podle názvu v popisu)
        for r in Recept.objects.all():
            # Získáme seznam ingrediencí podle názvu receptu (stejně jako v detailu)
            if r.nazev == 'Svíčková na smetaně':
                ingred = ['hovězí svíčková', 'kořenová zelenina', 'cibule', 'slanina', 'smetana', 'ocet', 'cukr', 'bobkový list', 'nové koření', 'pepř', 'sůl', 'olej', 'máslo']
            elif r.nazev == 'Guláš':
                ingred = ['hovězí kližka', 'cibule', 'česnek', 'sladká paprika', 'majoránka', 'rajčatový protlak', 'sůl', 'pepř', 'sádlo']
            elif r.nazev == 'Česnečka':
                ingred = ['česnek', 'brambory', 'zeleninový vývar', 'majoránka', 'sůl', 'pepř', 'chleba', 'sýr']
            elif r.nazev == 'Kuřecí řízek':
                ingred = ['kuřecí prsa', 'hladká mouka', 'vejce', 'strouhanka', 'sůl', 'pepř', 'olej na smažení', 'bramborová kaše']
            elif r.nazev == 'Štrúdl':
                ingred = ['listové těsto', 'jablka', 'rozinky', 'skořice', 'cukr', 'vejce', 'vanilková zmrzlina']
            else:
                ingred = []
            # Pokud uživatel má všechny ingredience na daný recept, zobrazíme ho
            if all(i in vybrane_ingredience for i in ingred):
                recepty.append(r)
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
