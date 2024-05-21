import unittest
import tkinter as tk
from wwbymm import MillionaireGame  # предполагая, что основной код сохранен в файле wwbymm.py
import random


class TestMillionaireGame(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.game = MillionaireGame(self.root)
        self.game.question_index = 0
        self.game.money = 0
        self.game.hint_used = False
        self.game.used_questions = set()
        self.game.game_over = False
        random.seed(42)  # фиксируем seed для воспроизводимости тестов

    def tearDown(self):
        self.root.destroy()

    def test_initial_setup(self):
        self.assertEqual(self.game.money, 0)
        self.assertEqual(self.game.question_index, 0)
        self.assertFalse(self.game.hint_used)
        self.assertEqual(len(self.game.used_questions), 0)

    def test_next_question(self):
        self.game.next_question()
        self.assertIsNotNone(self.game.current_question)
        self.assertEqual(len(self.game.current_answers), 4)
        self.assertEqual(len(self.game.used_questions), 1)

    def test_check_correct_answer(self):
        self.game.current_question = 'Какой газ преобладает в атмосфере Земли?'
        self.game.current_answers = ['Азот', 'Кислород', 'Гелий', 'Углекислый газ']
        correct_answer_index = self.game.current_answers.index('Азот')
        self.game.check_answer(correct_answer_index)
        self.assertEqual(self.game.money, 500)
        self.assertEqual(self.game.question_index, 1)

    def test_check_incorrect_answer(self):
        self.game.current_question = 'Какой газ преобладает в атмосфере Земли?'
        self.game.current_answers = ['Кислород', 'Азот', 'Гелий', 'Углекислый газ']
        incorrect_answer_index = self.game.current_answers.index('Кислород')
        self.game.check_answer(incorrect_answer_index)
        self.assertTrue(self.game.game_over)
        self.assertEqual(self.game.money, 0)

    def test_use_hint(self):
        self.game.current_question = 'Какой газ преобладает в атмосфере Земли?'
        self.game.current_answers = ['Азот', 'Кислород', 'Гелий', 'Углекислый газ']
        self.game.use_hint()
        enabled_buttons = [btn for btn in self.game.answer_buttons if btn['state'] == 'normal']
        self.assertEqual(len(enabled_buttons), 2)
        self.assertTrue(self.game.hint_used)
        self.assertEqual(self.game.hint_button['state'], 'disabled')


if __name__ == '__main__':
    unittest.main()