import bs4  # для парсинга информации
import requests  # для запроса


class Test:
    def __init__(self):
        self.data = dict()
        self.site_url = 'https://konstruktortestov.ru/'  # сайты с тестами

    def find_test(self, topic):
        text = []
        params = {
            'q': topic
        }
        response = requests.get(self.site_url + 'search', params=params)  # поиск тестов
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        page = soup.find('div', class_='page')
        if page.contents[3].text != 'Тесты не найдены!':
            tests = page.find('ul', class_='list-numder').findAll('li')
            i = 0
            for test in tests:
                i += 1
                name = test.find('p').text
                text.append(name)
                url = self.site_url + test.find('a')['href']
                self.data.setdefault(i, [name, url])
                if i > 10:
                    break
        else:
            return 'Тесты не найдены!'
        return text

    def give_test(self, choice):
        response = requests.get(self.data[choice][1])
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        count_of_questions = len(soup.find(id='pgn'))
        questions = []
        answers = []
        self.quest_answers = dict()
        for i in range(1, count_of_questions):
            question = soup.find(id=f'quest{i}').find('span', class_='what').text
            answers.append(list(map(lambda x:x.text, soup.find(id=f'quest{i}').find_all('li'))))
            questions.append(question)
        return questions, answers



