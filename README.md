# QA_internship_avito

## Структура репозитория

- Task1 - папка задания 1
  - bugs_task1.jpg - скриншот с багами
  - BUGS_FROM_SCREENSHOT.md - файл с описанием найденных багов

- Task2 - папка задания 2
  - TESTCASES.md - тесткейсы к заданию 2.2
  - test_create_search_edit.py - файл с автотестами к заданию 2.2
  - BUGS.md - файл с описанием найденных багов
  - requirements.txt - файл с модулями для запуска автотестов

- README.md - описание проекта и инструкция

## Инструкция для запуска автотестов

1) Проверить установлен ли python "python --version", если нет установить с официального сайта
2) Установить зависимости pip install -r requirements.txt
3) Посмотреть версию Google Chrome и скачать chromewebdriver, соответствующей версии с официального сайта
4) Проверить установлен ли git "git --version", если нет установить с официального сайта
5) Клонировать репозиторий git clone https://github.com/lukajin2001/QA_internship_avito.git
6) Перейти в папку с проектом "cd QA_internship_avito"
7) В файле test_create_search_edit.py указать путь к chromewebdriver, установленному ранее CHROMEDRIVER_PATH = "Путь"
8) Запустить автотест "pytest test_script.py"


