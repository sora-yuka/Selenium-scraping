from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from database import (
    session, AnnouncementsData, AnnouncementPosts, 
    AnnouncementPrices, AnnouncementPictures
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
    announcements = driver.find_elements(By.XPATH, "//div[contains(@class, 'container-results large-images')]")
    announcement_posts = driver.find_elements(By.XPATH, "//div[contains(@class, 'location')]")
    announcement_prices = driver.find_elements(By.XPATH, "//div[contains(@class, 'price')]")
    announcement_pictures = driver.find_elements(By.TAG_NAME, "img")
    
    """ Запись полученных данных в БД. """
    def save_announcement(announcements):
        for announcement in announcements:
            session.add(AnnouncementsData(Announcement.text))
            session.commit()
    save_announcement(Announcements)
    
    def save_announcement_price(announcement_prices):
        for announcement_price in announcement_prices:
            session.add(AnnouncementPrices(announcement_price.text))
            session.commit()
    save_announcement_price(announcement_prices)

    def save_announcement_post(announcement_posts):
        for announcement_post in announcement_posts:
            if "minutes" in announcement_post.text:
                announcement_post = datetime.now().date()
                announcement_post = announcement_post.strftime("%d%m%y")
            session.add(EnnouncementPosts(announcement_post.text))
            session.commit()
    save_ennouncement_post(announcement_posts)
    
    def save_announcement_picture(announcement_pictures):
        for announcement_picture in announcement_pictures:
            picture = announcement_picture.get_attribute("src")
            session.add(AnnouncementPictures(picture))
            session.commit()
    save_announcement_picture(announcement_pictures)
    
    
async def get_html_page(URI) -> None:
    """ Асинхронная функция отправляющая запрос на сайт и выводящий html код в терминале. """
    async with aiohttp.ClientSession() as session:
        async with session.get(URI) as response:
            print(await response.text())


def main():
    BASE_URL = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273"
    get_source_code(BASE_URL)  
    asyncio.run(get_html_page(BASE_URL))

""" Запуск основного проекта. """
if __name__ == "__main__":
    main()