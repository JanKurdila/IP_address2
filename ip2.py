import ipaddress
from collections import defaultdict

def rozober_subor(cesta_k_suboru):
    pouzivatelia = []

    # Otvorenie súboru na čítanie
    with open(cesta_k_suboru, 'r') as subor:
        riadky = subor.readlines()
    
    # Spracovanie riadkov súboru
    for riadok in riadky[1:]:
        casti = riadok.strip().split()
        
        # Vytvorenie slovníka pre používateľa
        pouzivatel = {
            'uzivatelske_meno': casti[0],
            'heslo': casti[1],
            'ip': casti[2],
            'subnet': casti[3],
            'krajina': casti[4],
            'datum_prihlasenia': casti[5],
            'datum_odhlasenia': casti[6],
            'cas_prihlasenia': casti[7],
            'cas_odhlasenia': casti[8]
        }
        pouzivatelia.append(pouzivatel)
    
    return pouzivatelia

def ziskaj_siet(ip, subnet):
    try:
        siet = ipaddress.ip_network(f'{ip}/{subnet}', strict=False)
        return siet.network_address
    except ValueError as e:
        print(f"Chyba s IP alebo subnet: {ip}/{subnet} - {e}")
        return None

def over_rovnaku_siet(ip1, subnet1, ip2, subnet2):
    siet1 = ziskaj_siet(ip1, subnet1)
    siet2 = ziskaj_siet(ip2, subnet2)
    if siet1 is None or siet2 is None:
        return False
    return siet1 == siet2

def hladaj_komponenty(pouzivatel, mapa_sieti, navstivene, komponenta):
    """
    Pomocná funkcia pre prehľadávanie používateľov v tej istej skupine
    pomocou algoritmu prehľadávania do hĺbky (DFS).

    :param pouzivatel: Počiatočný používateľ, od ktorého sa začína prehľadávanie
    :param mapa_sieti: Mapa sietí, kde sú uložené prepojenia medzi používateľmi
    :param navstivene: Množina používateľov, ktorí už boli navštívení
    :param komponenta: Množina, do ktorej sa pridávajú všetci používatelia v tej istej skupine
    """
    zasobnik = [pouzivatel]
    while zasobnik:
        aktualny = zasobnik.pop()
        if aktualny not in navstivene:
            navstivene.add(aktualny)
            komponenta.add(aktualny)
            zasobnik.extend(mapa_sieti[aktualny])

def najdi_skupiny_sieti(pouzivatelia):
    mapa_sieti = defaultdict(set)
    
    # Porovnanie používateľov a zistenie, či sú v rovnakej sieti
    for i in range(len(pouzivatelia)):
        for j in range(i + 1, len(pouzivatelia)):
            pouzivatel1 = pouzivatelia[i]
            pouzivatel2 = pouzivatelia[j]
            if over_rovnaku_siet(pouzivatel1['ip'], pouzivatel1['subnet'], pouzivatel2['ip'], pouzivatel2['subnet']):
                mapa_sieti[pouzivatel1['uzivatelske_meno']].add(pouzivatel2['uzivatelske_meno'])
                mapa_sieti[pouzivatel2['uzivatelske_meno']].add(pouzivatel1['uzivatelske_meno'])

    # Nájdite všetky prepojené komponenty
    navstivene = set()
    vsetky_komponenty = []
    
    for pouzivatel in mapa_sieti:
        if pouzivatel not in navstivene:
            komponenta = set()
            hladaj_komponenty(pouzivatel, mapa_sieti, navstivene, komponenta)
            vsetky_komponenty.append(komponenta)

    return vsetky_komponenty

def najdi_uzivatelov_v_rovnakych_sietach(cesta_k_suboru):
    pouzivatelia = rozober_subor(cesta_k_suboru)
    if not pouzivatelia:
        print("Nenašli sa žiadni používatelia.")
        return
    
    skupiny_sieti = najdi_skupiny_sieti(pouzivatelia)
    
    for skupina in skupiny_sieti:
        if len(skupina) > 1:  # Ignorovať jednotlivých používateľov
            skupina = sorted(skupina)
            print(f"Používatelia v rovnakej sieti: {', '.join(skupina)}")

# Hlavné vykonávanie
cesta_k_suboru = 'vstup.txt'
najdi_uzivatelov_v_rovnakych_sietach(cesta_k_suboru)
