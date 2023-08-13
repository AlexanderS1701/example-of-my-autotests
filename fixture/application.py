from selenium import webdriver

from pages.book_page import BookPageHelper
from pages.home_page import HomePageHelper
from pages.payment_page import PaymentPageHelper
from pages.session_page import SessionPageHelper
from pages.ticket_page import TicketPageHelper


class Application:

    def __init__(self):
        driver = webdriver.Chrome()
        driver.get("https://example-stage.team/")

        self.driver = driver
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()
        self.home_page = HomePageHelper(self)
        self.ticket_page = TicketPageHelper(self)
        self.book_page = BookPageHelper(self)
        self.payment_page = PaymentPageHelper(self)
        self.session_page = SessionPageHelper(self)

    def destroy(self):
        self.driver.quit()
