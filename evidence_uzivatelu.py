class Pojisteny:
# Třída pojištěného

    def __init__(self, jmeno, prijmeni, vek, telefonni_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefonni_cislo = telefonni_cislo
    # Kontruktor inicializujicí jméno, příjmení, věk a telefonní číslo
        

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, Věk: {self.vek}, tel.: {self.telefonni_cislo}"
    # reprezentace objektu (vracení řetězce)

    
class EvidencePojisteneho:
    def __init__(self, pojisteni_uzivatele):
        self.pojisteni_uzivatele = pojisteni_uzivatele
    # Konstruktor inicializující pojištěné uživatele


    def pridej_uzivatele(self, jmeno, prijmeni, vek, telefonni_cislo):
        # funkce přidání uživatele
        """
        vytvoření nové instance třídy Pojisteny a její přidání do seznamu
        :param jmeno:
        :param prijmeni:
        :param vek:
        :param telefonni_cislo:
        :return:
        """
        novy_uzivatel = Pojisteny(jmeno, prijmeni, vek, telefonni_cislo)
        self.pojisteni_uzivatele.append(novy_uzivatel)

    def najdi_uzivatele(self, jmeno = None, prijmeni = None):
        # fukce nalezení daného uživatele
        """
        možnost uživatele zadat buď jméno nebo příjmení nebo oboje pro lepší flexibilitu
        :param jmeno:
        :param prijmeni:
        :return:
        """
        for pojisteny_uzivatel in self.pojisteni_uzivatele: 
            if (jmeno and pojisteny_uzivatel.jmeno == jmeno) or (prijmeni and pojisteny_uzivatel.prijmeni == prijmeni):
                return pojisteny_uzivatel
            return None

    def zobraz_pojistene_uzivatele(self):
        # funkce zobrazení všech evidovaných uživatelů (vracení seznamu)
        """
        kontrola, zda seznam není prázdný, vrátíme textový řetězec, pokud ano
        vytvoření prázdného řetězce/proměnné vystup, kam se díky cyklu for, který prochází každého pojištěného, budou ukládat informace
        :return:
        """
        if not self.pojisteni_uzivatele:
            return "V evidenci nejsou žádní uživatelé evidováni"
        vystup = ""
        for uzivatel in self.pojisteni_uzivatele:
            vystup += f"Jméno: {uzivatel.jmeno}, Příjmení: {uzivatel.prijmeni}, Věk: {uzivatel.vek}, Telefon: {uzivatel.telefonni_cislo}\n"
        return vystup

