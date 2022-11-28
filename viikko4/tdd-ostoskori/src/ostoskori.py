from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.korissa = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        summa = 0
        for osto in self.korissa:
            tuote_korissa = self.korissa[osto]
            summa += tuote_korissa.lukumaara()
        return summa
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        lasku = 0
        for osto in self.korissa:
            tuote_korissa = self.korissa[osto]
            lasku += tuote_korissa.hinta()
        return lasku
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi() in self.korissa:
            self.korissa[lisattava.nimi()].muuta_lukumaaraa(1)
            return
        self.korissa[lisattava.nimi()] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        self.korissa[poistettava.nimi()].muuta_lukumaaraa(-1)
        if self.korissa[poistettava.nimi()].lukumaara() <= 0:
            del self.korissa[poistettava.nimi()]

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self.korissa.values())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
