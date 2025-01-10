import runner
import runner_and_tournament
import unittest

# RunnerTest` — это класс тестов для проверки функциональности бегунов.
# Он наследует от `unittest.TestCase`, что позволяет использовать методы для тестирования.

class RunnerTest(unittest.TestCase):
    is_frozen = False

    #  Пропуск тестов
    # Эта декорация позволяет пропустить тест, если `is_frozen` равно `True`.
    # Это полезно, если тесты временно не могут быть запущены.
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_walk = runner.Runner('Runner1')
        for i in range(10):
            runner_walk.walk()
        self.assertEqual(runner_walk.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_run = runner.Runner('Runner2')
        for i in range(10):
            runner_run.run()
        self.assertEqual(runner_run.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = runner.Runner("Runner1")
        runner2 = runner.Runner("Runner2")
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

# TournamentTest` — класс для тестирования турниров между бегунами. В нем также используются методы `unittest`.
class TournamentTest(unittest.TestCase):
    all_results = None
    is_frozen = False
    # Метод `setUpClass`
    # метод выполняется один раз перед запуском всех тестов в классе.Здесь создается словарь для хранения результатов.
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    # Этот метод выполняется перед каждым тестом и создает три экземпляра бегунов с разными параметрами.
    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усэйн', 10)
        self.andrey = runner_and_tournament.Runner('Андрей', 9)
        self.nik = runner_and_tournament.Runner('Ник', 3)

    # Этот метод выполняется один раз после всех тестов и выводит все результаты турниров.
    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                res[k] = str(v)
            print(res)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        first_run = runner_and_tournament.Tournament(90, self.usain, self.nik)
        result = first_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        second_run = runner_and_tournament.Tournament(90, self.andrey, self.nik)
        result = second_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        third_run = runner_and_tournament.Tournament(90, self.andrey, self.usain, self.nik)
        result = third_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result


if __name__ == '__main__':
    unittest.main()