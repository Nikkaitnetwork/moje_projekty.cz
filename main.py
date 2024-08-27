from evidence_uzivatelu import EvidencePojisteneho
# import 
evidence = EvidencePojisteneho([])
# vytvoření instance


class Akce:
    """
    Nová třída Akce (zde se odehrává komunikace s uživatelem - proto Akce)
    """
    while True:
        print("--------------------- \n")
        print("Evidence Pojištěných \n")
        print("--------------------- \n")
        print("Vyberte si akci:\n")
        print("1 - Přidat nového pojištěného\n")
        print("2 - Vypsat všechny pojištěné\n")
        print("3 - Vyhledat pojištěného\n")
        print("4 - Konec\n")
        # menu pro výběr uživatele
        volba_uzivatele = input("Zadejte číslo volby: ")
        # výběr volby z menu

        if volba_uzivatele == '1':  # přidání
            while True:
                jmeno = str(input("Zadejte jméno pojištěného: "))
                if len(jmeno) > 1 and all(cast.isalpha() or cast.isspace() for cast in jmeno):
                    """ 
                    zadání jména - podmínky: aby se jméno neskládalo z jednoho či méně znaků, dále v případě dvou jmen 
                    je jméno rozděleno jakoby na části, 
                    kde platí podmínky, aby řetězec (obě části) obsahoval pouze písmena a možné mezery (např: mezi dvěmi
                     jmény)
                    """
                    prijmeni = str(input("Zadejte příjmení: "))
                    if len(prijmeni) > 1 and prijmeni.isalpha():
                        """
                        zadání příjmení - podmínky: nesmí být kratší než jeden znak a musí obsahovat pouze písmena
                        """
                        vek = int(input("Zadejte věk: "))
                        if vek > 0 and vek < 125:
                            """
                            zadání věku - podmínky: nesmí být menší než 0 a zároveň menší než 125 (nejstarší člověk se 
                            dožil 122 let), aby někdo nezadal např: 1234
                            """
                            telefonni_cislo = (input("Zadejte telefonní číslo: "))
                            cislo_bez_mezer = telefonni_cislo.replace(" ", "")
                            if cislo_bez_mezer.startswith('+'):
                                cislo_bez_mezer = cislo_bez_mezer[4:]
                            if cislo_bez_mezer.isdigit() and len(cislo_bez_mezer) == 9:
                                """
                                Zadání telefonního čísla - podmínky: nejdříve z telefonního čísla pomocí replace 
                                odstraníme veškeré mezery (aby jsme je nemuseli počítat jako znaky) 
                                dále jsem zde chtěla naprogramovat možnost napsání předvolby s + = pokud tel. číslo 
                                začíná tímto symbolem, program s tím počítá a automaticky odstraní
                                první 4 znaky, pro zbytek čísla zde máme podmínku, aby se skládalo pouze z čísel a nebyl
                                o delší než 9 znaků
                                """
                                evidence.pridej_uzivatele(jmeno, prijmeni, vek, telefonni_cislo)
                                """
                                pokud vše bez problému projde, uloží se nový uživatel
                                """
                                print(f'Data byla uložena')
                                break
                            else: 
                                print(f"Zadané telefonní číslo: {telefonni_cislo}"
                                      f" obsahuje nepovolené znaky nebo nesplňuje podmínkuu délky (9 znaků).")
                        else: 
                            print("Věk není validní! Použijte pouze čísla větší než 0 a menší než 120.")
                    else:
                        print(f"Příjmení: {prijmeni}, obsahují nepovolené znaky!")
                else:
                    print(f"Jméno: {jmeno}, obsahuje nepovolené znaky nebo je moc krátké.")

                    """
                    zde jsou naprogramované chybové výstupy v případě porušení výšše napsaných podmínek (Error Handling)
                    """

        elif volba_uzivatele == '2':  # vypsání
            vystup = evidence.zobraz_pojistene_uzivatele()
            print(vystup)
            """
            zavoláme metodu pro vypsání uživatele
            """
            
        elif volba_uzivatele == '3':  # vyhledat
            jmeno = str(input("Zadejte jméno uživatele (nepovinné) :\n")).strip() 
            prijmeni = str(input("Zadejte příjmení uživatele (nepovinné) :\n")).strip()
            if not jmeno and not prijmeni:
                print("Musíte zadat alespoň jméno nebo příjmení")
            else:
                pojisteny_uzivatel = evidence.najdi_uzivatele(jmeno if jmeno else None, prijmeni if prijmeni else None)
                if pojisteny_uzivatel:
                    print(f"{pojisteny_uzivatel}")
                else:
                    print("Uživatel nebyl nalezen.")

            """
            zavolání metody pro vyhledání daného uživatele, možnost napsání pouze jména nebo příjmení, jinak se vrací 
            hodnota None
            """

        elif volba_uzivatele == '4':  # ukončení programu
            print("Konec programu")
            break

        else: 
            print("Neplatná volba, zkuste to znovu.")  # Error Handling

        print("Pro pokračování stiskněte libovolnou klávesu...")
        vstup = input()
        # pokračování stisknutím enter
