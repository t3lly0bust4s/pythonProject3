import tkinter as tk
from tkinter import messagebox
import random

# Вопросы и ответы
questions = {
    'Какой из этих цветов не является основным?': ['Зеленый', 'Красный', 'Желтый', 'Синий'],
    'Какой газ преобладает в атмосфере Земли?': ['Кислород', 'Углекислый газ', 'Азот', 'Гелий'],
    'Как звали вождя апачей, которого армия США сдала в плен в 1886 году?': ['Геронимо', 'Ситтинг Булл', 'Блэк Хок',
                                                                             'Красный Облако'],
    'Как называется персонаж из мультфильма "Ну, погоди!"?': ['Волк', 'Кот', 'Лиса', 'Медведь'],
    'Какая буква является первой в русском алфавите?': ['А', 'Б', 'В', 'Г'],
    'Кто написал роман "Война и мир"?': ['Лев Толстой', 'Федор Достоевский', 'Иван Тургенев', 'Антон Чехов'],
    'Столица Франции?': ['Париж', 'Берлин', 'Рим', 'Мадрид'],
    'Сколько планет в Солнечной системе?': ['8', '7', '9', '10'],
    'Какой элемент обозначается символом "O"?': ['Кислород', 'Золото', 'Кремний', 'Сера'],
    'Какое самое большое животное на Земле?': ['Синий кит', 'Африканский слон', 'Бегемот', 'Белый медведь'],
    'Кто основал компанию Microsoft?': ['Билл Гейтс', 'Стив Джобс', 'Марк Цукерберг', 'Ларри Пейдж'],
    'Какая планета ближе всего к Солнцу?': ['Меркурий', 'Венера', 'Земля', 'Марс'],
    'Как называется столица Японии?': ['Токио', 'Киото', 'Осака', 'Нагасаки'],
    'Какое число идет после 10?': ['11', '12', '9', '13'],
    'Кто написал музыку к балету "Лебединое озеро"?': ['Чайковский', 'Моцарт', 'Бетховен', 'Бах'],
    'В каком году произошла битва при Ватерлоо?': ['1815', '1805', '1795', '1825'],
    'Кто разработал теорию относительности?': ['Альберт Эйнштейн', 'Исаак Ньютон', 'Галилео Галилей', 'Никола Тесла'],
    'Какая самая глубокая точка в мире?': ['Марианская впадина', 'Бермудский треугольник', 'Мёртвое море', 'Байкал'],
    'Какой язык программирования используется для разработки Android приложений?': ['Java', 'Swift', 'Python', 'C++'],
    'Кто написал пьесу "Гамлет"?': ['Уильям Шекспир', 'Джордж Оруэлл', 'Франсуа Рабле', 'Марк Твен'],
    'Кто был первым человеком, ступившим на Луну?': ['Нил Армстронг', 'Юрий Гагарин', 'Базз Олдрин', 'Алан Шепард'],
    'Какая страна имеет самую большую площадь?': ['Россия', 'Канада', 'Китай', 'США'],
    'Как называется процесс преобразования из твердого состояния в газообразное, минуя жидкое?': ['Сублимация',
                                                                                                  'Конденсация',
                                                                                                  'Испарение',
                                                                                                  'Плавление'],
    'Кто создал первую механическую модель Солнечной системы?': ['Николай Коперник', 'Галилео Галилей', 'Исаак Ньютон',
                                                                 'Архимед'],
    'Кто написал роман "Преступление и наказание"?': ['Федор Достоевский', 'Лев Толстой', 'Антон Чехов',
                                                      'Иван Тургенев'],
    'Как называется самая большая пустыня в мире?': ['Антарктическая пустыня', 'Сахара', 'Гоби', 'Калахари'],
    'Какая страна первой отправила человека в космос?': ['СССР', 'США', 'Китай', 'Франция'],
    'Как называется химический элемент с символом Au?': ['Золото', 'Аргон', 'Уран', 'Серебро'],
    'Как называется самая высокая гора в мире?': ['Эверест', 'К2', 'Канченджанга', 'Макалу']
}

# Правильные ответы
correct_answers = {
    'Какой из этих цветов не является основным?': 'Зеленый',
    'Какой газ преобладает в атмосфере Земли?': 'Азот',
    'Как звали вождя апачей, которого армия США сдала в плен в 1886 году?': 'Геронимо',
    'Как называется персонаж из мультфильма "Ну, погоди!"?': 'Волк',
    'Какая буква является первой в русском алфавите?': 'А',
    'Кто написал роман "Война и мир"?': 'Лев Толстой',
    'Столица Франции?': 'Париж',
    'Сколько планет в Солнечной системе?': '8',
    'Какой элемент обозначается символом "O"?': 'Кислород',
    'Какое самое большое животное на Земле?': 'Синий кит',
    'Кто основал компанию Microsoft?': 'Билл Гейтс',
    'Какая планета ближе всего к Солнцу?': 'Меркурий',
    'Как называется столица Японии?': 'Токио',
    'Какое число идет после 10?': '11',
    'Кто написал музыку к балету "Лебединое озеро"?': 'Чайковский',
    'В каком году произошла битва при Ватерлоо?': '1815',
    'Кто разработал теорию относительности?': 'Альберт Эйнштейн',
    'Какая самая глубокая точка в мире?': 'Марианская впадина',
    'Какой язык программирования используется для разработки Android приложений?': 'Java',
    'Кто написал пьесу "Гамлет"?': 'Уильям Шекспир',
    'Кто был первым человеком, ступившим на Луну?': 'Нил Армстронг',
    'Какая страна имеет самую большую площадь?': 'Россия',
    'Как называется процесс преобразования из твердого состояния в газообразное, минуя жидкое?': 'Сублимация',
    'Кто создал первую механическую модель Солнечной системы?': 'Николай Коперник',
    'Кто написал роман "Преступление и наказание"?': 'Федор Достоевский',
    'Как называется самая большая пустыня в мире?': 'Антарктическая пустыня',
    'Какая страна первой отправила человека в космос?': 'СССР',
    'Как называется химический элемент с символом Au?': 'Золото',
    'Как называется самая высокая гора в мире?': 'Эверест'
}

# Градация награды за правильные ответы
prize_money = [500, 1000, 2000, 3000, 5000, 10000, 15000, 25000, 50000, 100000, 200000, 400000, 800000, 1500000,
               3000000]


class MillionaireGame:
    def __init__(self, root):
        # Инициализация основного окна
        self.root = root
        self.root.title("Кто хочет стать миллионером")
        self.money = 0  # Начальная сумма выигрыша
        self.question_index = 0  # Индекс текущего вопроса
        self.current_question = None  # Текущий вопрос
        self.current_answers = []  # Варианты ответов на текущий вопрос
        self.hint_used = False  # Флаг, указывающий на использование подсказки
        self.used_questions = set()  # Множество для хранения использованных вопросов

        # Создание метки для вопроса
        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack(pady=20)

        # Создание кнопок для ответов
        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.answer_buttons.append(button)

        # Создание кнопки для подсказки 50/50
        self.hint_button = tk.Button(root, text="Подсказка 50/50", command=self.use_hint)
        self.hint_button.pack(pady=20)

        # Начать игру с первого вопроса
        self.next_question()

    def next_question(self):
        # Проверка на окончание игры
        if self.question_index >= len(prize_money):
            messagebox.showinfo("Поздравляем!", "Вы ответили на все вопросы и выиграли 3 000 000 рублей!")
            self.root.destroy()  # Закрытие окна
            return

        # Включение кнопки подсказки, если она еще не использована
        if not self.hint_used:
            self.hint_button["state"] = "normal"

        # Выбор нового вопроса, который еще не был использован
        remaining_questions = [q for q in questions.keys() if q not in self.used_questions]
        if not remaining_questions:
            messagebox.showinfo("Поздравляем!", f"Вы ответили на все вопросы и выиграли {self.money} рублей!")
            self.root.destroy()  # Закрытие окна
            return

        self.current_question = random.choice(remaining_questions)
        self.used_questions.add(self.current_question)
        self.current_answers = questions[self.current_question][:]
        random.shuffle(self.current_answers)  # Перемешивание ответов

        # Обновление текста вопроса и кнопок ответов
        self.question_label.config(text=self.current_question)
        for i, answer in enumerate(self.current_answers):
            self.answer_buttons[i].config(text=answer, state="normal")

    def check_answer(self, index):
        selected_answer = self.current_answers[index]  # Выбранный ответ
        correct_answer = correct_answers[self.current_question]  # Правильный ответ

        if selected_answer == correct_answer:
            # Правильный ответ: обновление суммы выигрыша и индекса вопроса
            self.money = prize_money[self.question_index]
            self.question_index += 1
            messagebox.showinfo("Правильный ответ!", f"Вы выиграли {self.money} рублей!")
            self.next_question()
        else:
            # Неправильный ответ: игра заканчивается
            messagebox.showerror("Неправильный ответ", f"Вы выиграли {self.money} рублей.")
            self.root.destroy()

    def use_hint(self):
        if self.hint_used:
            return  # Если подсказка уже использована, ничего не делаем

        correct_answer = correct_answers[self.current_question]  # Правильный ответ
        incorrect_answers = [a for a in self.current_answers if a != correct_answer]  # Неправильные ответы
        remove_answers = random.sample(incorrect_answers,
                                       len(incorrect_answers) - 1)  # Удаляем все, кроме одного неправильного ответа

        # Деактивируем кнопки с неверными ответами
        for answer in remove_answers:
            index = self.current_answers.index(answer)
            self.answer_buttons[index].config(text="", state="disabled")

        # Деактивируем кнопку подсказки и устанавливаем флаг использования
        self.hint_button["state"] = "disabled"
        self.hint_used = True


# Создание основного окна и запуск игры
if __name__ == "__main__":
    root = tk.Tk()
    game = MillionaireGame(root)
    root.mainloop()