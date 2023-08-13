from selenium import webdriver

from pages.home_page import HomePageHelper
from pages.ticket_page import TicketPageHelper


class Application:

    def __init__(self):
        driver = webdriver.Chrome()
        driver.get("https://examplelink-stage.team/")

        self.driver = driver
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()
        self.home_page = HomePageHelper(self)
        self.ticket_page = TicketPageHelper(self)

    def destroy(self):
        self.driver.quit()
