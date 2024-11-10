# Домашнее задание по теме "Систематизация и пропуск тестов".
from HumanMoveTest import Runner, Tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_walk1 = Runner("Name1")
        for n in range(10):
            test_walk1.walk()
        self.assertEqual(test_walk1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_run1 = Runner("Name2")
        for n in range(10):
            test_run1.run()
        self.assertEqual(test_run1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_walk2 = Runner("Name3")
        test_run2 = Runner("Name4")
        for n in range(10):
            test_walk2.walk()
            test_run2.run()
        self.assertNotEqual(test_walk2, test_run2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tourne1(self):
        tourne_1 = Tournament(self.distans, self.usein, self.nik)
        result = tourne_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['test_tourne1'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tourne2(self):
        tourne_2 = Tournament(self.distans, self.andrey, self.nik)
        result = tourne_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['test_tourne2'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tourne3(self):
        tourne_3 = Tournament(self.distans, self.usein, self.andrey, self.nik)
        result = tourne_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['test_tourne3'] = result
