# Internetové technologie 2018

## Zadání semetrální práce z předmětu KKY/ITE

Semestrální práce bude na téma [Web scraping][1] a [fulltextové vyhledávání][2].
Vaším úkolem bude:

1) vytvoření *"robota"* , který bude stahovat HTML (např. zču, wikipedie, atp.), - **15b**
1) vytvoření modulu, který zpracuje HTML, získá obsah stránky a nalezne odkazy, - **20b**
    > Pro vyčištění HTML je možné využít knihovnu, např. [Beautiful Soup][3],
    > ale kreativitě se meze "nekladou".
    * nalezené odkazy budou opět zpracovány *"robotem"*,
    > "Zanoření" bude omezeno např. časově nebo hloubkou (**4**).
    > Myslete na křížové odkazy.
1) získaná data (obsah, odkazy) budou uloženy na disk, případně do databáze, - **15b**
1) získaná data zobrazenit pomocí webové stránky, kde bude přítomno pole pro zadávání
dotazu (full-text) a místo pro zobrazení výsledků + iframe s originálem (např. jeden
pro aktuálně vybraný). - **20b**
    > Data mezi serverem a klientem budou předávána ve formátu **JSON** nebo XML,
    > ale doporučujeme JSON, protože ten prohlížeče zpracovávají automaticky.
    >
    > Layout stránky je plně na Vás, ale Google je dobrým příkladem.
    >
    > Pokud je někdo zdatnější, tak může být jako challenge bráno našeptávání,
    > realizované například pomocí websocketů.

Rozhodně byste neměli vše naprogramovat jako jeden velký modul. Jednak se v tom
nevyznáme a i pro Vás bude težší vše správně "uřídit". Doporučení tedy je, mít vše
v modulech a spouštět vše samostatně. *"Robot"* získá data, ta se následně zpracují
dalším modulem a zaindexují. Mezitím pořád beží webový server, který obhospodařuje
požadavky na vyhledávání a přistupuje k, v té době aktuálním, datům.

> Protože jsme kybernetici a máme rádi data, tak stojí za zvážení zobrazení statistik,
> např. počet "indexovaných" stránek, atp.

### Požadavky

* Python 3
* Při odevzdávání semestrální práce bude součastí popis funkce (minimálně jaké stránky jsou stahovány) a **podrobný** návod jak Vaše řešení spustit. V návodu bude i "výpis" toho co je potřebné k jeho chodu (klidně může být součastí [conda environment][4]), ušetříte nám tím spoustu nervů při spuštění. Berte to tak, že odevzdáváte produkt zákazníkovi.
* Jako server využijte Tornado, ale pokud budete chtít zapojit i něco jiného (třeba Node.js), tak můžete.
* Fulltextové vyhledávání naprogramujte sami, využití externích knihoven opodstatněte.
    > Pokud máté zkušenosti, tak doporučujeme použití nějaké databáze.

> **TIP**: Obecně se snažte využívat knihovny/moduly, které jsou obecně využívány. Pokud to má na githubu jednotky hvězd, tak radši použijte něco jineho.
>
> **POZNÁMKA**: V případě potřeby bude zadání doplněno o další podrobnější informace.

[1]: https://en.wikipedia.org/wiki/Web_scraping
[2]: https://cs.wikipedia.org/wiki/Fulltextov%C3%A9_vyhled%C3%A1v%C3%A1n%C3%AD
[3]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
[4]: https://conda.io/docs/user-guide/tasks/manage-environments.html
