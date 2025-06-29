# Dokumentacja Aplikacji My Library

Aplikacja Flask do zarządzania kolekcją książek umożliwiająca dodawanie, przeglądanie, edytowanie i usuwanie książek z osobistej biblioteki. System pozwala na przechowywanie informacji o tytule, autorze, ocenie oraz obrazie okładki każdej książki.

## Opis Funkcji

### Funkcjonalności Główne

Aplikacja oferuje pełny zestaw operacji CRUD (Create, Read, Update, Delete) dla zarządzania kolekcją książek. Użytkownicy mogą przeglądać wszystkie książki w swojej kolekcji na stronie głównej, gdzie pozycje są automatycznie sortowane alfabetycznie według tytułu. Funkcja dodawania nowych książek umożliwia wprowadzenie kompletnych informacji o każdej pozycji, włączając tytuł, autora, ocenę numeryczną oraz ścieżkę do obrazu okładki.

System edycji pozwala na modyfikację oceny istniejących książek, co jest szczególnie użyteczne gdy użytkownik chce zaktualizować swoją opinię o przeczytanej pozycji. Funkcjonalność usuwania umożliwia trwałe usunięcie książek z kolekcji, gdy nie są już potrzebne. Wszystkie operacje są obsługiwane przez intuicyjny interfejs webowy wykorzystujący Bootstrap do responsywnego designu.

### Architektura Systemu

Aplikacja została zbudowana w oparciu o framework Flask z wykorzystaniem wzorca MVC (Model-View-Controller). Model danych jest implementowany poprzez SQLAlchemy ORM, co zapewnia bezpieczne i efektywne operacje na bazie danych SQLite. Kontrolery są realizowane przez funkcje route w Flask, które obsługują logikę biznesową aplikacji. Widoki są implementowane jako szablony HTML z wykorzystaniem systemu templateowania Jinja2.

Konfiguracja aplikacji obejmuje ustawienia bazy danych SQLite, dozwolone rozszerzenia plików obrazów oraz ścieżkę do przesyłanych plików. System jest skonfigurowany do działania na wszystkich interfejsach sieciowych (0.0.0.0) na porcie 5000, co umożliwia dostęp z innych urządzeń w sieci lokalnej.

## Schemat Bazy Danych

### Model Book

Struktura tabeli `books` w bazie danych składa się z następujących kolumn:


| Pole | Typ | Ograniczenia | Opis |
| :-- | :-- | :-- | :-- |
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unikalny identyfikator książki |
| title | VARCHAR(250) | NOT NULL, UNIQUE | Tytuł książki |
| author | VARCHAR(250) | NOT NULL | Autor książki |
| rating | FLOAT | NOT NULL | Ocena książki (liczba zmiennoprzecinkowa) |
| image | VARCHAR(300) | NOT NULL | Ścieżka do obrazu okładki |

Klucz główny `id` jest automatycznie generowany przez bazę danych i służy jako unikalny identyfikator każdej książki w systemie. Pole `title` ma ograniczenie unikalności, co oznacza, że nie można dodać dwóch książek o identycznym tytule. Pole `rating` przechowuje ocenę jako liczbę zmiennoprzecinkową, co pozwala na precyzyjne ocenianie książek. Pole `image` przechowuje ścieżkę względną lub bezwzględną do pliku obrazu okładki książki.

### Relacje i Indeksy

Aktualnie model danych zawiera jedną tabelę bez relacji z innymi tabelami. System może być w przyszłości rozszerzony o dodatkowe tabele dla autorów, kategorii czy wydawnictw z odpowiednimi kluczami obcymi. Automatyczny indeks jest tworzony na kolumnie `id` jako klucz główny, a dodatkowy indeks może być utworzony na kolumnie `title` ze względu na ograniczenie unikalności.

## Diagramy

### Diagram Architektury Systemu

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Przeglądarka  │    │   Flask Server  │    │   SQLite DB     │
│                 │    │                 │    │                 │
│  - HTML/CSS/JS  │◄──►│  - Routes       │◄──►│  - Books Table  │
│  - Bootstrap    │    │  - Templates    │    │  - CRUD Ops     │
│  - Forms        │    │  - SQLAlchemy   │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```


### Diagram Przepływu Danych

```
Start
  ↓
Użytkownik wysyła żądanie HTTP
  ↓
Flask Router identyfikuje odpowiednią funkcję
  ↓
Funkcja przetwarza żądanie
  ↓
[Czy wymagane operacje DB?] ──Yes──► SQLAlchemy ORM ──► SQLite
  ↓ No                                    ↓
Renderowanie szablonu ◄──────────────────┘
  ↓
Zwrócenie odpowiedzi HTTP
  ↓
End
```


### Diagram ERD (Entity Relationship Diagram)

```
┌─────────────────────────────────┐
│            Book                 │
├─────────────────────────────────┤
│ + id: INTEGER (PK)              │
│ + title: VARCHAR(250) (UNIQUE)  │
│ + author: VARCHAR(250)          │
│ + rating: FLOAT                 │
│ + image: VARCHAR(300)           │
└─────────────────────────────────┘
```


## Przypadki Użycia

### Przypadek Użycia 1: Przeglądanie Kolekcji

**Aktor:** Użytkownik aplikacji
**Cel:** Wyświetlenie wszystkich książek w kolekcji
**Przebieg:**

1. Użytkownik otwiera stronę główną aplikacji (/)
2. System pobiera wszystkie książki z bazy danych
3. Książki są sortowane alfabetycznie według tytułu
4. System wyświetla listę książek z wszystkimi informacjami
5. Użytkownik może zobaczyć tytuł, autora, ocenę i okładkę każdej książki

**Warunki wstępne:** Aplikacja jest uruchomiona i dostępna
**Warunki końcowe:** Użytkownik widzi kompletną listę swojej kolekcji książek

### Przypadek Użycia 2: Dodawanie Nowej Książki

**Aktor:** Użytkownik aplikacji
**Cel:** Dodanie nowej książki do kolekcji
**Przebieg:**

1. Użytkownik klika link/przycisk "Dodaj książkę"
2. System przekierowuje na stronę formularza dodawania (/add)
3. Użytkownik wypełnia formularz: tytuł, autor, ocena, ścieżka obrazu
4. Użytkownik przesyła formularz (POST)
5. System waliduje dane i tworzy nowy rekord w bazie danych
6. System przekierowuje użytkownika na stronę główną
7. Nowa książka pojawia się na liście

**Warunki wstępne:** Użytkownik ma dostęp do formularza dodawania
**Warunki końcowe:** Nowa książka jest zapisana w bazie danych i widoczna na liście

### Przypadek Użycia 3: Edycja Oceny Książki

**Aktor:** Użytkownik aplikacji
**Cel:** Zmiana oceny istniejącej książki
**Przebieg:**

1. Użytkownik klika link "Edytuj" przy wybranej książce na stronie głównej
2. System przekierowuje na stronę edycji z wypełnionym formularzem (/edit?book_id=X)
3. Użytkownik modyfikuje ocenę książki
4. Użytkownik przesyła formularz (POST)
5. System aktualizuje rekord w bazie danych
6. System przekierowuje użytkownika na stronę główną
7. Zmieniona ocena jest widoczna na liście

**Warunki wstępne:** Książka istnieje w bazie danych
**Warunki końcowe:** Ocena książki jest zaktualizowana

### Przypadek Użycia 4: Usuwanie Książki

**Aktor:** Użytkownik aplikacji
**Cel:** Usunięcie książki z kolekcji
**Przebieg:**

1. Użytkownik klika link "Usuń" przy wybranej książce na stronie głównej
2. System wykonuje żądanie GET do /delete?book_id=X
3. System lokalizuje książkę w bazie danych
4. System usuwa rekord z bazy danych
5. System przekierowuje użytkownika na stronę główną
6. Książka nie jest już widoczna na liście

**Warunki wstępne:** Książka istnieje w bazie danych
**Warunki końcowe:** Książka jest trwale usunięta z kolekcji

## API

### Endpoint: GET /

**Opis:** Strona główna wyświetlająca wszystkie książki w kolekcji
**Metoda HTTP:** GET
**Parametry:** Brak
**Odpowiedź:** Renderuje szablon `index.html` z listą wszystkich książek sortowanych alfabetycznie
**Kod statusu:** 200 OK

```python
# Przykład użycia wewnętrznego
books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
return render_template('index.html', books=books)
```


### Endpoint: GET/POST /add

**Opis:** Dodawanie nowej książki do kolekcji
**Metoda HTTP:** GET (wyświetlenie formularza), POST (przesłanie danych)

**GET /add:**

- **Parametry:** Brak
- **Odpowiedź:** Renderuje szablon `add.html` z formularzem dodawania
- **Kod statusu:** 200 OK

**POST /add:**

- **Parametry formularzowe:**
    - `name` (string): Tytuł książki
    - `author` (string): Autor książki
    - `rating` (float): Ocena książki
    - `image` (string): Ścieżka do obrazu okładki
- **Odpowiedź:** Przekierowanie do strony głównej (/)
- **Kod statusu:** 302 Found (przekierowanie)


### Endpoint: GET/POST /edit

**Opis:** Edycja oceny istniejącej książki
**Metoda HTTP:** GET (wyświetlenie formularza), POST (aktualizacja danych)

**GET /edit:**

- **Parametry URL:**
    - `book_id` (integer): ID książki do edycji
- **Odpowiedź:** Renderuje szablon `edit.html` z danymi książki
- **Kod statusu:** 200 OK lub 404 Not Found (jeśli książka nie istnieje)

**POST /edit:**

- **Parametry URL:**
    - `book_id` (integer): ID książki do edycji
- **Parametry formularzowe:**
    - `rating` (float): Nowa ocena książki
- **Odpowiedź:** Przekierowanie do strony głównej (/)
- **Kod statusu:** 302 Found (przekierowanie)


### Endpoint: GET /delete

**Opis:** Usuwanie książki z kolekcji
**Metoda HTTP:** GET
**Parametry URL:**

- `book_id` (integer): ID książki do usunięcia
**Odpowiedź:** Przekierowanie do strony głównej (/)
**Kod statusu:** 302 Found (przekierowanie) lub 404 Not Found (jeśli książka nie istnieje)

```python
# Przykład wywołania
# GET /delete?book_id=5
book_selected = db.get_or_404(Book, book_id)
db.session.delete(book_selected)
db.session.commit()
return redirect(url_for('home'))
```


## Instalacja i Uruchomienie

### Wymagania

```bash
pip install flask flask-sqlalchemy flask-bootstrap5
```


### Konfiguracja

Aplikacja automatycznie tworzy bazę danych SQLite o nazwie `books-collection.db` w katalogu głównym projektu.

### Uruchomienie

```bash
python main.py
```

Aplikacja będzie dostępna pod adresem `http://localhost:5000` lub `http://0.0.0.0:5000`.



