# Documentation main page

## Table of contents

1. [Assignment][01]
2. [References][03]

## Authors

* Jakub Kratochvíl
* Marek Lovčí
* Tomáš Honzík

## Web user interface

Jako uživatelské prostředí pro zadávání dotazů k vyhledání slouží HTML stránka založená na [Bootstrap 4.1][50]. Tento HTML/CSS farmework nám vyřešil veškerou práci se vzhledem aplikace. Nebylo nutné navrhovat vzhled a následně ho stylovat pomocí CSS, vše bylo po stažení připraveno k použití.

## Poznámky k programu

1) Aby bylo zřejmé, že probíhá načítání stránky do iframe, do prostoru jeho načtení jsme přidali 'loader', který slouží jako zpětná vazba pro uživatele, zdali se iframe stále načítá, nebo jestli se již načetl a daná stránka jej pouze nepodporuje.

2) Z důvodů irelevantnosti (nemožnosti zobrazit iframe a nesmyslnost získaných informací) a bugu kvůli kterému byly stránky z facebooku po stažení do souboru poněkud velké (cca 15 MB), jsme vynechali z url ke stažení Youtube a facebook.

3) Pro scrapování textu je v bs4 funkce 'get_text()', bohužel nefunguje podle očekávání a vrací list, kde každá položka je jeden znak. Proto tuto funkci nepoužíváme.

4) Při opětovném spuštění websrapping robota se stránky duplikují v případě, že se ručně nesmaže obsah složky storage.

[01]: /docs/assignment.md
[03]: /docs/references.md

[50]: https://getbootstrap.com/
