# Домашнее задание по теме "Методы Юнит-тестирования"
# Цель: освоить методы, которые содержит класс TestCase.
from HumanMoveTest import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.usein = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

        self.distans = 90

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_tourne1(self):
        tourne_1 = Tournament(self.distans, self.usein, self.nik)
        result = tourne_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['test_tourne1'] = result

    def test_tourne2(self):
        tourne_2 = Tournament(self.distans, self.andrey, self.nik)
        result = tourne_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['test_tourne2'] = result

    def test_tourne3(self):
        tourne_3 = Tournament(self.distans, self.usein, self.andrey, self.nik)
        result = tourne_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['test_tourne3'] = result

