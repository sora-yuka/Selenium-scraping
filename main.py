from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from database import session, ScrapData, AdditionalData
import aiohttp
import asyncio

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def get_source_code(URI) -> None:
    """Функция для скрапинга данных с сайтов."""
    driver.get(URI)
    
    titles = driver.find_elements(By.TAG_NAME, "h4")
    chapters = driver.find_elements(By.XPATH, "//div[contains(@class, 'updates__item')]//div[contains(@class, 'updates__body')]")
#*  ^^^^^^^^^^^^^^^^^^^^^^^
    """Получение данных."""
    
    for title in titles:
        result = title.text
        title = ScrapData(result)
        session.add(title)
        session.commit()
    
    for chapter in chapters:
        result = chapter.text
        chapter = AdditionalData(result, title.id)
        session.add(chapter)
        session.commit()
    """Запись полученных данных в БД."""
    
    
async def get_html_page(URI) -> None:
    """Функция отправляющая запрос на сайт и выводящий html код в терминале."""
    async with aiohttp.ClientSession() as session:
        async with session.get(URI) as response:
            print(await response.text())
            

def main():
    BASE_URL = "https://ranobelib.me/?section=home-updates"
    get_source_code(BASE_URL)
    asyncio.run(get_html_page(BASE_URL))
    
if __name__ == "__main__":
    main()