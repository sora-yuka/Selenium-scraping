from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from database import (
    session, EnnouncementsData, EnnouncementPosts, 
    EnnouncementPrices, EnnouncementPictures
)
from datetime import datetime
import aiohttp
import asyncio

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def get_source_code(URI) -> None:
    """ Функция для скрапинга данных с сайтов. """
    driver.get(URI)
    
    """ Получение данных. """
    ennouncements = driver.find_elements(By.XPATH, "//div[contains(@class, 'container-results large-images')]")
    ennouncement_posts = driver.find_elements(By.XPATH, "//div[contains(@class, 'location')]")
    ennouncement_prices = driver.find_elements(By.XPATH, "//div[contains(@class, 'price')]")
    ennouncement_pictures = driver.find_elements(By.TAG_NAME, "img")
    
    """ Запись полученных данных в БД. """
    def save_ennouncement(ennouncements):
        for ennouncement in ennouncements:
            session.add(EnnouncementsData(ennouncement.text))
            session.commit()
    save_ennouncement(ennouncements)
    
    def save_ennouncement_price(ennouncement_prices):
        for ennouncement_price in ennouncement_prices:
            session.add(EnnouncementPrices(ennouncement_price.text))
            session.commit()
    save_ennouncement_price(ennouncement_prices)

    def save_ennouncement_post(ennouncement_posts):
        for ennouncement_post in ennouncement_posts:
            session.add(EnnouncementPosts(ennouncement_post.text))
            session.commit()
    save_ennouncement_post(ennouncement_posts)
    
    def save_ennouncement_picture(ennouncement_pictures):
        for ennouncement_picture in ennouncement_pictures:
            picture = ennouncement_picture.get_attribute("src")
            session.add(EnnouncementPictures(picture))
            session.commit()
    save_ennouncement_picture(ennouncement_pictures)
    
    
async def get_html_page(URI) -> None:
    """ Асинхронная функция отправляющая запрос на сайт и выводящий html код в терминале. """
    async with aiohttp.ClientSession() as session:
        async with session.get(URI) as response:
            print(await response.text())


def main():
    BASE_URL = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273"
    get_source_code(BASE_URL)
    asyncio.run(get_html_page(BASE_URL))
    
if __name__ == "__main__":
    main()