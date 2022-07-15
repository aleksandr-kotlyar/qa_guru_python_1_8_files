1. [Скачивание файла с помощью requests](#1-скачивание-файла)
2. [Сохранение содержимого с именем](#2-Сохранение-содержимого-с-именем)
3. [Закрытие файла после записи](#3-Закрытие-файла-после-записи)
4. [Скачивание файла браузером](#4-Скачивание-файла-браузером)
5. [Определение размера файла](#5-определение-размера-файла)
6. [Определение абсолютного пути к файлу](#6-определение-абсолютного-пути-к-файлу)
7. [Определение абсолютного пути к текущей директории](#7-Определение-абсолютного-пути-к-текущей-директории)
8. [Работа с путями: добавление пути](#8-работа-с-путями-добавление-пути)
9. [Чтение/запись в файл](#9-чтение-запись-в-файл)
10. [Работа с CSV](#10-работа-с-csv)
11. [Работа с PDF](#11-Работа-с-PDF)
12. [Работа с XLS](#12-работа-с-xls)
13. [Работа с XLSX](#13-работа-с-xlsx)
14. [Работа с ZIP](#14-Работа-с-zip)


## 1. Скачивание файла

Python предоставляет различные модули, такие как urllib, requests и другие, для загрузки файлов из интернета. Я собираюсь использовать Python библиотеку requests для эффективной загрузки файлов с URL-адресов.

Давайте начнем с пошаговой процедуры загрузки файлов с URL-адресов с использованием библиотеки requests.

### Импорт модуля
```python
import requests
```

### Запрос ссылки или URL
```python
url = 'https://selenium.dev/images/selenium_logo_square_green.png'
r = requests.get(url, allow_redirects=True)
```

## 2. Сохранение содержимого с именем
```python
open('selenium.png', 'wb').write(r.content)
```
сохраняет файл как selenium.png.

### Пример
```python
import requests

url = 'https://selenium.dev/images/selenium_logo_square_green.png'
r = requests.get(url, allow_redirects=True)

open('selenium.png', 'wb').write(r.content)
```

### Результат
Мы видим, что файл загружен (png) в наш текущий рабочий каталог.

## 3. Закрытие файла после записи
Если вы заметили, мы не закрыли файл, с которым мы работали в приведенном выше примере. И хотя Python автоматически закрывает файл, если ссылочный объект(переменная) файла выделяется для другого файла, стандартная практика — закрытие открытого файла, поскольку закрытый файл снижает риск необоснованного изменения или чтения.
В Python есть метод close() для закрытия файла. Метод close() можно вызывать более одного раза, и если какая-либо операция выполняется с закрытым файлом, возникает ошибка ValueError.
Перепишем наш код так, чтобы закрыть открытый файл после записи в него.
```python
import requests

url = 'https://selenium.dev/images/selenium_logo_square_green.png'
r = requests.get(url, allow_redirects=True)

file = open('selenium.png', 'wb')
   
# Запись в файл
file.write(r.content)
 
# Закрытие файла
file.close()
```
Теперь, если попытаемся в него записать - получим ошибку.
```
>>> file.write("Попытка записать в закрытый файл")
ValueError: I/O operation on closed file.
```
Лучше всего использовать конструкцию with
```python
import requests

url = 'https://selenium.dev/images/selenium_logo_square_green.png'
r = requests.get(url, allow_redirects=True)

with open('selenium.png', 'wb') as new_file:
    new_file.write(r.content)

```
Это своего рода best-practice в python.

С with файл всегда автоматически будет закрываться и код читабельнее и короче.
## 4. Скачивание файла браузером

В selene, в отличие от selenide нет отдельного магического метода download, который универсально будет скачивать файлы и из Chrome, и из Firefox. Однако, про него пока и не спрашивали. Значит он не очень-то и был нужен питонистам. ;) 

Давайте посмотрим как с помощью python скачать файл из браузера Chrome.
```python
from selenium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": '/Users/aleksandr/PyCharmProjects/qa_guru_python_1_8/resources',
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

browser.config.driver = driver

browser.open("https://demoqa.com/upload-download")
browser.s("#downloadButton").click()
```
Видим, что файл не качается. Что-то тут не так. Возможно, браузер слишком быстро закрывается.

Проверим, добавив небольшой sleep.
```python
import time

time.sleep(1)
```
В питоне слипы в секундах. Запускаем, смотрим. Видим, что файл теперь успевает скачаться.
На самом деле слипы - "зло" и с ними нужно быть аккуратными. Здесь по хорошему стоит написать функцию с умным ожиданием, которая периодически проверяет не появился ли файл и завершает выполнение по таймауту или когда файл появился. Как ее реализовать - подумайте сами. А мы двигаемся дальше.
Сейчас мы узнали как скачать файл с помощью браузера, и какие могут быть подводные камни.

## 5. Определение размера файла
```python
import os

os.path.getsize('selenium.png')
```

## 6. Определение абсолютного пути к файлу
```python
os.path.abspath(__file__)
```

## 7. Определение абсолютного пути к текущей директории
```python
os.path.dirname(os.path.abspath(__file__))
```

## 8. Работа с путями: добавление пути

```python
current_dir = os.path.dirname(os.path.abspath(__file__))

# склейка пути от текущей директории к ./resources внутри нее 
os.path.join(current_dir, 'resources')
```

## 9. Чтение/запись в файл
```python
# запись в файл
with open('example.txt', 'w') as f:
    f.write('abc')

# чтение файла по строкам
f = open('example.txt')
for row in f:
    print(row)

# чтение всего файла
with open('new_file.txt') as f:
    text = f.read()
    assert 'abc' in text
```

## 10. Работа с CSV
```python
import csv

with open('resources/eggs.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
    csvwriter.writerow(['Alex', 'Serj', 'Yana'])

with open('resources/SampleCSVFile_11kb.csv') as csvfile:
    csvfile = csv.reader(csvfile)
    for r in csvfile:
        print(r)
```

## 11. Работа с PDF
Для работы с PDF-файлами нам понадобится подключить стороннюю библиотеку PyPDF2.

Для открытия PDF-файла используем класс PdfReader и передаем в его конструктор путь к нашему PDF.

Далее обращаясь к объекту reader, мы видим все методы класса, что мы можем сделать с файлом.
```python
from PyPDF2 import PdfReader

reader = PdfReader("./resources/docs-pytest-org-en-latest.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(text)
print(number_of_pages)

assert "pytest Documentation" in text
```

## 12. Работа с XLS
В питоне для каждой задачи свой инструмент и библиотека.
Поэтому для работы с XLS и с XLSX нам потребуются разные библиотеки.

Для XLS-файлов установим библиотеку xlrd

Файлы открываются следующим образом:

```python
import xlrd

book = xlrd.open_workbook('resources/file_example_XLS_10.xls')
```

В XLS-таблицах есть элементы:
- Листы — их может быть несколько в одной таблице;
- Столбцы;
- Строки;
- Ячейки.

![](https://raw.githubusercontent.com/qa-guru/knowledge-base/main/img/les8/les_xls.png)

К каждому элементу можно обратиться с помощью вызова метода:

- листы — sheetnames();
- строчки — getRow();
- столбцы — getCell();
- ячейка — пересечение строки и столбца.

Примеры:
```python
import xlrd

book = xlrd.open_workbook('resources/file_example_XLS_10.xls')
print(f'Количество листов {book.nsheets}')
print(f'Имена листов {book.sheet_names()}')
sheet = book.sheet_by_index(0)
print(f'Количество столбцов {sheet.ncols}')
print(f'Количество строк {sheet.nrows}')
print(f'Пересечение строки 9 и столбца 1 = {sheet.cell_value(rowx=9, colx=1)}')
# печать всех строк по очереди
for rx in range(sheet.nrows):
    print(sheet.row(rx))
```

## 13. Работа с XLSX
```python

from openpyxl import load_workbook
workbook = load_workbook('resources/file_example_XLSX_50.xlsx')
sheet = workbook.active
print(sheet.cell(row=3, column=2).value)
```

## 14. Работа с ZIP
Для работы с zip в python есть встроенная библиотека zipfile.
Архив открывается передачей в конструктор класса ZipFile пути к архиву.

```python
from zipfile import ZipFile

zip_ = ZipFile('resources/hello.zip')
print(zip_.namelist())
text = zip_.read('Hello.txt')
print(text)
zip_.close()

with ZipFile('resources/hello.zip') as myzip:
    myzip.extract('Hello.txt')
```
Из архива можно получить список заархивированных объектов, прочитать объекты не распаковывая их, распаковать, упаковать и многое другое.
По завершении работы архивом его стоит закрыть. 