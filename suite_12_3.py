# Домашнее задание по теме "Систематизация и пропуск тестов".
# Задача "Заморозка кейсов"
import unittest
import tests_12_3

humanMoveTest = unittest.TestSuite()
humanMoveTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
humanMoveTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(humanMoveTest)
