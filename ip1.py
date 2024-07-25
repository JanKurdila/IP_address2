import ipaddress

def rozloz_subor(subor_cesta):
    uzivatelia = []
    with open(subor_cesta, 'r') as subor:
        riadky = subor.readlines()

    #hlavicka = riadky[0].strip().split()  # Prvý riadok (hlavička)

    for riadok in riadky[1:]:  # Začni spracovávať riadky od druhého riadku
        casti = riadok.strip().split()
        
        uzivatel = {
                'uzivatelske_meno': casti[0],
                'heslo': casti[1],
                'ip': casti[2],
                'subnet': casti[3],
                'krajina': casti[4],
                'datum_prihlasenia': casti[5],
                'datum_odhlasenia': casti[6],
                'cas_prihlasenia': casti[7],
                'cas_odhlasenia': casti[8]}
        uzivatelia.append(uzivatel)
    
    return uzivatelia

def ziskaj_siet(ip, subnet):
    try:
        siet = ipaddress.ip_network(f'{ip}/{subnet}', strict=False)
        return siet.network_address
    except ValueError as e:
        print(f"Chyba s IP alebo subnetom: {ip}/{subnet} - {e}")
        return None

def skontroluj_rovnaku_siet(ip1, subnet1, ip2, subnet2):
    siet1 = ziskaj_siet(ip1, subnet1)
    siet2 = ziskaj_siet(ip2, subnet2)
    if siet1 is None or siet2 is None:
        return False
    return siet1 == siet2

def najdi_uzivatelov_z_rovnakej_siete(subor_cesta):
    uzivatelia = rozloz_subor(subor_cesta)
    if not uzivatelia:
        print("Neboli nájdení žiadni užívatelia.")
        return
    
    videne_dvojice = set()
    
    for i in range(len(uzivatelia)):
        for j in range(i + 1, len(uzivatelia)):
            uzivatel1 = uzivatelia[i]
            uzivatel2 = uzivatelia[j]
            if uzivatel1['uzivatelske_meno'] == uzivatel2['uzivatelske_meno']:
                continue  # Preskoč ak ide o rovnakého užívateľa
            if skontroluj_rovnaku_siet(uzivatel1['ip'], uzivatel1['subnet'], uzivatel2['ip'], uzivatel2['subnet']):
                # Vytvor unikátny kľúč pre dvojicu
                dvojica_kluc = tuple(sorted([uzivatel1['uzivatelske_meno'], uzivatel2['uzivatelske_meno']]))
                if dvojica_kluc not in videne_dvojice:
                    videne_dvojice.add(dvojica_kluc)
                    print(f"Užívatelia {uzivatel1['uzivatelske_meno']} a {uzivatel2['uzivatelske_meno']} sú v rovnakej sieti.")

# Hlavná exekúcia
subor_cesta = 'vstup.txt'
najdi_uzivatelov_z_rovnakej_siete(subor_cesta)
