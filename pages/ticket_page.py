from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators import base_page_locators as hp
from locators import ticket_page_locators as tp


class TicketPageHelper:
    def __init__(self, app):
        self.app = app

    def wait_search_end(self):
        driver = self.app.driver
        wait = WebDriverWait(driver, 50)
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, hp.SEARCH_RESULTS)))

    def check_ticket_list(self):
        ticket_list = self.app.driver.find_elements(By.XPATH, tp.TICKET_LIST)
        assert ticket_list[0].is_displayed()
