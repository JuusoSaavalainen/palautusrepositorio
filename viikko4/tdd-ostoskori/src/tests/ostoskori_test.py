import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        
    #step 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(),  0)
        
    #step 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        

    #step 3
    def test_yhden_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

        
    #step 4
    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        kalja = Tuote("Kalja", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kalja)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

        
    #step 5
    def test_Kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        kalja = Tuote("Kalja", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kalja)
        self.assertEqual(self.kori.hinta(), 8)

        
    #step 6
    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

        
    #step 7
    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_2_kertaa_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)

    #step 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        # testaa että metodin palauttaman listan pituus 1

    # step 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)
        # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.

    #setp 10
    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        kalja = Tuote("Kalja", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kalja) 
        
        ostos = self.kori.ostokset()

        self.assertEqual(len(ostos), 2)

    #step 11
    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito) 
        ostos = self.kori.ostokset()

        self.assertEqual(len(ostos), 1)
    
    #step 12 
    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lukumäärä_2(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito) 
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)