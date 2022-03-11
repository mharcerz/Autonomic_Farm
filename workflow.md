# Workflow

*Wszystko to możecie wyklikać w Pycharmie ręcznie (ale tego już nie wytłumacznie) i tu wtedy macie ściągawke co robić po kolei*

## Tworzenie nowej funkcjonalnośći
**Nie puszujemy bezpośrednio nic na mastera!!!**
1. Pullujemy żeby mieć najnowszą wersje repo: ``git pull``
2. Tworzymy nowego brancha i przechodzimy na niego: ``git checkout -b nazwa_określająca_funkcjonalność`` 
3. Dodajemy komity na tą gałź (według instrukcji "Dodawanie zmian")
4. Tworzymy pull requesta
5. Albo sprawdzamy / prosimy kogoś o sprawdzenie czy okej, albo mergujemy gotową funkcjonalnośc do mastera

## Dodawanie zmian

1. Sprawdzamy jakie pliki mamy "nie śledzone" (na czerwono), gotowe do wrzucenia: ``git status``

**NIE WRZUCAMY ŚMIECI NA REPO TYPU .idea/.venv i tp.**

2. Dodajemy pliki: ``git add nazwa_pliku`` (jak sie upewnimy, że wrzucamy tylko potrzbene pliki to można ``git add .``)
3. Tworzymy commita: ``git commit -m zwięzły_opis_zmian``
4. Puszujemy na repo: ``git push origin nazwa_gałęzi``

## Klonowanie repo
*Polecam tak zrobić nawet jak później będziecie wyklikiwac reszte w Pycharmie*
1. Odpalamy git.wmi.amu.pl i kopiujemy linka do repo (http, chyba ze mamy skonfigurowany klucz ssh)
2. Odpalamy git basha
3. Przechodzimy do lokalizacji gdzie będziemy chcieli sklonowac repo
4. Klonujemy repo: ``git clone link_do_repo``
5. Odpalamy Pycharemem sklonowane repo i reszte już możemy wyklikiwac z Pychrma

*Jak coś jeszcze nie będziecie umieć to piszcie, to się dopisze, żeby wszyscy wiedzieli*
