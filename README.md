# Internetové technologie 2018

Semestrální práce k předmětu KKY/ITE, vytvářená v trojčlenných týmech. Cílem této aplikace je fulltextové vyhledávání nad daty získaných z webových stránek. Více informací [zde][1].

## Popis programu

Program se skládá ze 2 částí, první částí je webscaping, který prohledá do šířky strom stránek pod stránkou startovní a uloží na disk data potřebná pro část druhou. Druhou částí je samotná webová aplikace sloužící k vyhledávání textu v uložených webových stránkách.

## Install

### Dependencies

Seznam nadstandartních balíčků nad balíčky 'Anaconda Distribution' nutných k chodu programu je uveden v souboru 'requirements.txt'.

## Spuštění webscrapping robota

Přes příkazovou řádku se program spouští příkazem `> python -m ite` v adresáři programu. Pro více info viz [docs.python.org][2]. V případě použití PyCharm IDE spustit soubor `__main__.py`. Pro změnu startovní stránky změňte proměnnou 'start_url' v souboru `__main__.py` v metodě 'main()' a pro změnu hloubky prohledávání změňte proměnnou 'max_depth' ve stejném souboru a metodě.

## Spuštění serveru

Funkčnost aplikace je podmíněna staženými daty (pomocí webscrapping robota). Přes příkazovou řádku se server spouští příkazem `> python -m ite.server` v adresáři programu. V případě použití PyCharm IDE spustit soubor `server.py`.

## Spuštění klientské aplikace

Webová aplikace je přístupná pod url `localhost:8885`.

[1]: https://github.com/mareklovci/ite/wiki
[2]: https://docs.python.org/3.6/using/cmdline.html
