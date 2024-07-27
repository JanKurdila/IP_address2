# Sú viacere zariadenia (PC) z jednej siete?

Od správcu siete jedného nemenovaného serveru sme získali vstupný súbor s názvom vstup.txt. Hlavička obsahuje týchto 9 stĺpcov, ktoré sú medzi sebou oddelené jednou medzerou.

prihlasovacie_meno heslo IP_adresda Maska Stat den_prihlasenia den_odhlasenia cas_prihlasenia cas_odhlasenia

<b>Úlohou</b> je napísať kód, kt. vypíše  zariadenia, resp. (PC) , ktoré boli z jednej spoločnej siete.

<b>Poznámka:</b>    Preštudujte si najprv:  https://github.com/JanKurdila/IP_address
                                                            
Návrh na riešenie:

        1) Prečítať a rozložiť súbor podľa stĺpcov hlavičky
        2) Ziskať sieť na základe IP zariadenia a masky
        3) Skontrolovať či sú dve zariadenia v jednej sieti
        4) Nájsť uživateľov z rovnakej siete (teda prechádzať a porovnávať všetkých so všetkými)             


## Po prvom riešeni
Náš výstup je celkom dobrý len by sme ho potrebovali upraviť...
