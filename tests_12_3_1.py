import HomeWork2Mod12 as hw
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.Us = hw.Runner("Усэйн", 10)
        self.Andr = hw.Runner("Андрей", 9)
        self.Nik = hw.Runner("Ник", 3)


    @classmethod
    def tearDownClass(cls):
        print("Да")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        us_andr_nik = hw.Tournament(90, self.Us, self.Andr, self.Nik)
        us_andr_nik.start()
        if self.assertTrue(True):
            print("Андрей")
        else:
            print("Ник")


if __name__ == "__main__":
    unittest.main()
