# Домашнее задание по теме "Простые Юнит-Тесты"
from module_12_1 import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_walk1 = Runner("Name1")
        for n in range(10):
            test_walk1.walk()
        self.assertEqual(test_walk1.distance, 50)

    def test_run(self):
        test_run1 = Runner("Name2")
        for n in range(10):
            test_run1.run()
        self.assertEqual(test_run1.distance, 100)

    def test_challenge (self):
        test_walk2 = Runner("Name3")
        test_run2 = Runner("Name4")
        for n in range(10):
            test_walk2.walk()
            test_run2.run()
        self.assertNotEqual(test_walk2, test_run2.distance)
