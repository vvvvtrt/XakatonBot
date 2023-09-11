token = ''
token_ai = ''

arr_faculty = ["ИКН", "ЭкоТех", "ИНМиН", "ГИ", "ЭУПП", "ИБО", "ИНОБР"]
arr_directions = {"ИКН": ["ИВТ", "ПМ", "БИ"], "ЭкоТех": ["КИ", "ПВОК", "ПМИО", "СПМИП"], "ИНМиН": ["Ф", "НИН"],
                  "ГИ": ["ЭИЭ", "ГД", "ФПГИНП", "М", "ТМИО", "ТБ", "ЭИЭ"], "ЭУПП": ["ЭИУ", "ТГ"],
                  "ИБО": ["МИМ", "ФИА", "ЭРСС", "ЭТ", "М"], "ИНОБР": ["МЧМ", "МЦМ", "ЛПЧЦМ", "ОМД", "ПМКМП", "ИСТ", "ЭУНП"]}
arr_degree = {"Бакалавр": ["1", "2", "3", "4"], "Магистр": ["1", "2"], "Специалист": ["1", "2", "3", "4", "5"]}

arr_hobby = {"🎨Творчество🎨": ["Фотографии", "Видеосъёмка", "Музыка", "Рукоделие", "Рисование", "Танцы"],
             "🎬Хобби🎬": ["Компьютерные игры", "Кино и сериалы", "Книги", "Кулинария"],
             "⚽️Спорт⚽️": ["Футбол", "Баскетбол", "Волейбол", "Хоккей", "Фитнес", "Йога"],
             "📚Учёба📚": ["Математика", "Физика", "Программирование", "Вычислительные машины", "Английский"]
             }
arr_varia = {"Домашние животные": ["Кошка", "Собака", "Хомяк", "Рыбка"],
             "Любимая еда": ["Пельмени", "Пицца", "Шаурма", "Сладости"],
             "Любимые мемы": ["Мем 1", "Мем 2", "Мем 3", "Мем 4"]}
arr_search = ["Подготовка к сессии", "Поиск по интересам", "Поиск по родному городу", "Поиск компании для прогулки"]
arr_place = ['Парк', "Кино", "Музей", "Театр", "Cпортивные мероприятия"]

if __name__ == '__main__':
    for i in arr_hobby:
        print(i)
        print(*arr_hobby[i], sep="\n")
