# Django Recepty

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-4.x-green)
![License](https://img.shields.io/badge/license-MIT-orange)

**Django Recepty** je webová aplikace postavená na frameworku Django, která slouží k ukládání, správě a sdílení receptů. Uživatelé mohou vytvářet, upravovat a prohlížet recepty, přidávat ingredience a postup přípravy. Projekt je ideální pro milovníky vaření a vývojáře, kteří chtějí pracovat s jednoduchou Django aplikací.

## Funkce
- **Správa receptů**: Vytváření, úprava a mazání receptů.
- **Ingredience a postupy**: Příprava receptů s podrobným seznamem ingrediencí a kroků.
- **Responzivní design**: Aplikace je přizpůsobena pro použití na mobilních zařízeních i desktopu.
- **Autentizace uživatelů**: Registrace a přihlášení pro personalizované funkce (volitelné, pokud je implementováno).

## Požadavky
- Python 3.8+
- Django 4.x
- SQLite (výchozí databáze, lze změnit na PostgreSQL nebo jinou)
- Další závislosti uvedeny v `requirements.txt`

## Instalace

1. Naklonujte si repozitář:
   ```bash
   git clone https://github.com/TomasHoles/Django-recepty.git
   cd Django-recepty
   ```

2. Vytvořte virtuální prostředí a aktivujte ho:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Na Windows: venv\Scripts\activate
   ```

3. Nainstalujte závislosti:
   ```bash
   pip install -r requirements.txt
   ```

4. Proveďte migrace databáze:
   ```bash
   python manage.py migrate
   ```

5. (Volitelné) Vytvořte superuživatele pro přístup do administrace:
   ```bash
   python manage.py createsuperuser
   ```

6被人: Spusťte vývojový server:
   ```bash
   python manage.py runserver
   ```

7. Otevřete prohlížeč a přejděte na `http://127.0.0.1:8000`.

## Struktura projektu
- **`recepty/`**: Hlavní Django aplikace obsahující modely, pohledy a šablony.
- **`templates/`**: HTML šablony pro frontend.
- **`static/`**: Statické soubory (CSS, JavaScript, obrázky).
- **`manage.py`**: Hlavní skript pro správu projektu.

## Použití
- Přidejte nový recept přes formulář na webu.
- Prohlížejte recepty v seznamu nebo podle kategorií (pokud je implementováno).
- Přihlaste se jako administrátor na `/admin` pro správu obsahu.

## Přispívání
Rád uvítám jakékoli příspěvky! Pokud chcete přispět:
1. Forkněte tento repozitář.
2. Vytvořte novou větev (`git checkout -b feature/nova-funkce`).
3. Proveďte změny a commitněte (`git commit -m "Přidána nová funkce"`).
4. Pushněte změny (`git push origin feature/nova-funkce`).
5. Vytvořte Pull Request.

## Licence
Tento projekt je licencován pod [MIT licencí](LICENSE).

## Kontakt
Pokud máte dotazy nebo návrhy, kontaktujte mě na [email@example.com](mailto:email@example.com) nebo vytvořte issue na GitHubu.
