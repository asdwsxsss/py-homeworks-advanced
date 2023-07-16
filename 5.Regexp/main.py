from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)


## 1. Выполните пункты 1-3 задания.
phone_pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d*)?\)?')
text_pattern = re.compile(
    r'(\w+[А-яЁё])\s*\,*(\w+[А-яЁё])\s*\,*(\w+[А-яЁё])*\,*(\w+[А-яЁё])*\,*(\w+[А-яЁё]\w+[А-яЁё –]*'
    r'\–*\s*)*\,*(\+*\d\s*\(*\d+\)*\-*\s*\d+\-*\d+\-*\d+\s*\(*\w*\.*\s*\d*\)*)*\,*([a-zA-Z0-9_.+-]'
    r'+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)*')

listt = []
for i in range(len(contacts_list)):
    if i == 0:
        listt.append(contacts_list[i])
    else:
        line = ','.join(contacts_list[i])
        result = re.search(text_pattern, line)
        listt.append(list(result.groups()))
        if listt[i][5] is not None:
            listt[i][5] = phone_pattern.sub(r'+7(\2)\3-\4-\5\6\7\8', listt[i][5])
     

final_list = []
for i in range(len(listt)):
    for j in range(len(listt)):
        if listt[i][0] == listt[j][0]:
            listt[i] = [x or y for x, y in zip(listt[i], listt[j])]
    if listt[i] not in final_list:
        final_list.append(listt[i])


## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(final_list)