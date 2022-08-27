# pip install lxml
# pip install requests
# pip install bs4

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
        self.count_of_questions = len(soup.find(id='quests'))  # чтобы и блиц тесты проходили
        self.quest_answers = dict()
        self.has_img = False
        for i in range(1, self.count_of_questions + 1):
            quest = soup.find(id=f'quest{i}')
            question = quest.find('span', class_='what').text
            question_img_url = quest.find('img')
            if question_img_url != None:
                self.has_img = True
                img = open('img/1.png', 'wb')
                question_img = requests.get(self.site_url + question_img_url.attrs['src']).content
                img.write(question_img)
                img.close()
            answers = list(map(lambda x: x.text, soup.find(id=f'quest{i}').find_all('li')))
            yield question, answers

            # out = open('1.img', "wb")
            # out.write(question_img.content)
            # out.close()

