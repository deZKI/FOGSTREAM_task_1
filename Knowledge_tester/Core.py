import bs4  # для парсинга информации
import requests  # для запроса


class Test:

    def __init__(self):
        self.data = dict()
        self.site_url = 'https://konstruktortestov.ru/'  # сайты с тестами
        topic = input('Выберете тему для теста: ')
        params = {
            'q': topic
        }
        response = requests.get(self.site_url + 'search', params=params)  # поиск тестов
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        self.page = soup.find('div', class_='page')
        if self.page.contents[3].text != 'Тесты не найдены!':
            tests = self.page.find('ul', class_='list-numder').findAll('li')
            i = 0
            for test in tests:
                i += 1
                name = test.find('p').text
                url = self.site_url + test.find('a')['href']
                self.data.setdefault(i, [name, url])
            print(self.data)
        else:
            print('Тесты не найдены!')

    def give_test(self):
        print('Выберете тест по номеру')
        for test in self.data.items():
            print(test[0], test[1][0])
        choice = int(input())
        response = requests.get(self.data[choice][1])
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        count_of_questions = len(soup.find(id='pgn'))
        quest_answers = dict()
        for i in range(1, count_of_questions):
            question = soup.find(id=f'quest{i}').find('span', class_='what').text
            answers = list(map(lambda x:x.text, soup.find(id=f'quest{i}').find_all('li')))
            quest_answers.setdefault(question, answers)
        for question, answers in quest_answers.items():
            print(question, '\n', f'Варианты ответов:{answers}', '\n')

