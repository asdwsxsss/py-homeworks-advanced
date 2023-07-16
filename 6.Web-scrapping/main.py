import requests
import bs4
import fake_headers
import json

def to_json(file):
    with open('vacancy.json', 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii=False, indent=4)

def main():
    main_link = 'https://spb.hh.ru/search/vacancy?text=Python+django+flask&salary=&area=1&area=2&ored_clusters=true&page='
    pages = 4
    for p in range(pages):
        linkk = main_link + str(p)
        headers = fake_headers.Headers(browser='YaBrowser', os='win').generate()
        response = requests.get(linkk, headers=headers).text
        main_html = bs4.BeautifulSoup(response, "lxml")
        vacancy_tags = main_html.find_all('div', class_='serp-item')
        vacancy_file = finder(vacancy_tags)
    to_json(vacancy_file)

vacancy = []

def finder(vacancy_tags):
    for vacancy_tag in vacancy_tags:
        vacancy_title_tag = vacancy_tag.find('a', class_='serp-item__title')
        title = vacancy_title_tag.text
        link = vacancy_tag.find('a')['href']
        salary = vacancy_tag.find('span', {'data-qa':"vacancy-serp__vacancy-compensation"})
        salary_text = ''
        if salary == None:
            salary_text = 'ЗП не указана'
        else:
            salary_text = salary.text
        company = vacancy_tag.find('a', class_='bloko-link bloko-link_kind-tertiary').text
        city = vacancy_tag.find('div', {'data-qa':'vacancy-serp__vacancy-address'}).text
        vacancy.append({
            'Вакансия:' : title,
            'Компания:' : company,
            'Зарплата:' : salary_text,
            'Ссылка:': link,
            'Город:': city
        })
    return vacancy

main()
