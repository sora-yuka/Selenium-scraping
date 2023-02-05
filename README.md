# Скрапинг сайта kijiji 

### ***kijiji*** - это канадский сайт объявлений. Были спарсены объявления :newspaper:, url картинкок :camera:, цены объявлений :money_with_wings: и дата создания поста :date:.
___
## Использовальнные библиотеки.


![Flutter](https://img.shields.io/badge/-Selenium-yellow?style=for-the-badge&logo=python) 

![Flutter](https://img.shields.io/badge/-Webdriver_manager-yellow?style=for-the-badge&logo=python)

![Flutter](https://img.shields.io/badge/-SqlAlchemy-yellow?style=for-the-badge&logo=python)

![Flutter](https://img.shields.io/badge/-Aiohttp-yellow?style=for-the-badge&logo=python)

![Flutter](https://img.shields.io/badge/-Asyncio-yellow?style=for-the-badge&logo=python)

___
### Для хранения данных использовалась база данных PostgreSql. 
___

### Чтобы запустить проект необходимо:

- Скопировать репозиторий.
  ```
  git clone hhtps://github.com:sora-yuka/selenium_scraping.git
  ```

- Создать и активировать виртуальное окружение.
  
  ```virtualenv venv```  или  ```python -m venv venv```

- Загрузить необходимые зависимости.
  
  ```
  pip install -r requirements.txt
  ```

- Подключить бд в файле проекта.

  + инструкция указана в самом проекте :wink:

- Запустить проект.

  ```
  python main.py
  ```