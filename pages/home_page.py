from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import home_page_locators as hp


class HomePageHelper:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def check_header(self):
        header = self.driver.find_elements(By.CSS_SELECTOR, hp.HEADER)
        condition = 'Авиабилеты в Казахстане' in header[0].text
        assert condition, 'Отсутствует заголовок "Авиабилеты в Казахстане"'

    def check_placeholders(self):
        placeholders_data = [
            {'element_name': hp.ARR_INPUT, 'placeholder': 'Куда'},
            {'element_name': hp.DEP_INPUT, 'placeholder': 'Откуда'},
        ]
        for p in placeholders_data:
            self.check_placeholder(p['element_name'], p['placeholder'])

    def check_placeholder(self, element_name, expected_placeholder):
        elements = self.driver.find_elements(By.CSS_SELECTOR, element_name)
        condition = elements[0].get_attribute('placeholder') == expected_placeholder
        assert condition, f'Отсутствует плейсхолдер "{element_name}"'

    def check_city(self, key, city_name):
        data = {
            'departure': {'element_name': hp.DEP_INPUT, 'description': 'город отправления'},
            'arrival': {'element_name': hp.ARR_INPUT, 'description': 'город прибытия'},
        }
        city_data = data[key]
        elements = self.driver.find_elements(By.CSS_SELECTOR, city_data['element_name'])
        condition = city_name in elements[0].get_attribute('value')
        assert condition, f"Текст в форме '{city_data['element_name']}' не совпадает с ожидаемым"

    def check_swap_city_button(self):
        swap_button = self.driver.find_elements(By.CSS_SELECTOR, hp.SWAP_CITY_BUTTON)
        assert swap_button[0].is_displayed(), 'Кнопка "swap_button" не отображается на странице'

    def check_text_content_in_passengers_button(self, pax_class='Эконом', amount='1'):
        class_data = self.driver.find_elements(By.CSS_SELECTOR, hp.CLASS_SPAN)
        paxes_data = self.driver.find_elements(By.CSS_SELECTOR, hp.PASSENGERS_AMOUNT)
        assert class_data[0].text == pax_class, f'Класс в кнопке не соответствует {pax_class}'
        assert amount in paxes_data[0].text, f'Количесво паксов не соответствует {amount}'

    def check_hotel_checkbox(self):
        hotel_checkbox = self.driver.find_elements(By.CSS_SELECTOR, hp.HOTEL_CHECKBOX)
        hc_is_displayed = hotel_checkbox[0].is_displayed()
        assert hc_is_displayed, 'Кнопка "hotel_checkbox" не отображается на странице'

    def check_search_button(self):
        search_button = self.driver.find_elements(By.CSS_SELECTOR, hp.SEARCH_BUTTON)
        sb_is_displayed = search_button[0].is_displayed()
        assert sb_is_displayed, 'Кнопка "search_button" не отображается на странице'

    def check_search_history_is_missing(self):
        locator = (By.XPATH, hp.HISTORY_1)
        wait = WebDriverWait(self.driver, 3)
        try:
            wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            assert False, 'История поиска отображается, хотя не должна'

    def check_search_history(self):
        history_1 = self.driver.find_elements(By.XPATH, hp.HISTORY_1)
        assert history_1[0].is_displayed(), 'История поиска не отображаятся, хотя должна'

    def select_city(self, field_selector, city, index):
        selected_city = self.driver.find_elements(By.CSS_SELECTOR, field_selector)
        selected_city[index].send_keys(city)
        first_city_in_list = self.driver.find_elements(By.CSS_SELECTOR, hp.FIRST_CITY_IN_LIST)
        assert first_city_in_list[0].is_displayed(), 'город не нейден'
        first_city_in_list[0].click()

    def select_departure(self, city, index=0):
        """На вход принимает код или название города"""
        self.select_city(hp.DEP_INPUT, city, index)

    def select_arrival(self, city, index=0):
        """На вход принимает код или название города"""
        self.select_city(hp.ARR_INPUT, city, index)

    def click_swap_button(self):
        swap_button = self.driver.find_element(By.CSS_SELECTOR, hp.SWAP_CITY_BUTTON)
        swap_button.click()

    def click_search_button(self):
        search_button = self.driver.find_element(By.CSS_SELECTOR, hp.SEARCH_BUTTON)
        search_button.click()

    def click_history_1_button(self):
        history_1_button = self.driver.find_element(By.XPATH, hp.HISTORY_1)
        history_1_button.click()

    def click_complex_route_button(self):
        complex_route_button = self.driver.find_element(By.CSS_SELECTOR, hp.COMPLEX_ROUTE_BUTTON)
        complex_route_button.click()

    def click_remove_complex_route_button(self, remove):
        remove_complex_route_button = self.driver.find_elements(
            By.CSS_SELECTOR, hp.REMOVE_COMPLEX_ROUTE_BUTTON
        )
        remove_complex_route_button[remove].click()

    def check_complex_route_button(self):
        complex_route_button = self.driver.find_elements(By.CSS_SELECTOR, hp.COMPLEX_ROUTE_BUTTON)
        crb_is_enabled = complex_route_button[0].is_enabled()
        if len(self.driver.find_elements(By.CSS_SELECTOR, hp.DEP_INPUT)) >= 4:
            assert not crb_is_enabled, "Добавление пятого перелета должно быть невозможным"
        else:
            assert crb_is_enabled, "Недоступна кнопка добавления перелета, хотя должна быть"

    def check_remove_complex_route_button(self):
        remove_complex_route_button = self.driver.find_elements(
            By.CSS_SELECTOR, hp.REMOVE_COMPLEX_ROUTE_BUTTON
        )
        is_displayed = remove_complex_route_button[0].is_displayed()
        assert is_displayed, 'Кнопка удаления перелета не отображаятся, хотя должна'

    def click_passengers_data_input(self):
        passengers_inp_btn = self.driver.find_element(By.CSS_SELECTOR, hp.PASSENGERS_DATA_INPUT)
        passengers_inp_btn.click()
        window_passengers = self.driver.find_element(By.CSS_SELECTOR, hp.WINDOW_PASSENGERS)
        assert window_passengers.is_displayed(), 'Окно выбора пассажиров не открылось'

    def check_passengers_data_input(self):
        passengers_data_input = self.driver.find_elements(
            By.CSS_SELECTOR, hp.PASSENGERS_DATA_INPUT
        )
        pdi_is_displayed = passengers_data_input[0].is_displayed()
        assert pdi_is_displayed, 'Кнопка "passengers_data_input" не отображается на странице'

    def click_default_pax_btn(self):
        default_pax_btn = self.driver.find_element(By.CSS_SELECTOR, hp.DEFAULT_PAX_BTN)
        default_pax_btn.click()

        class_attribute = default_pax_btn.get_attribute('class')
        assert " " in class_attribute, 'Кнопка "Обычный" не выделена синим'

        number_of_tariffs = self.driver.find_elements(By.CSS_SELECTOR, hp.PASSENGERS_TITLE)
        assert len(number_of_tariffs) == 3, 'Количество тарифов не равняется трем'

        econom_btn = self.driver.find_element(By.CSS_SELECTOR, hp.ECONOM_BTN)
        assert econom_btn.is_displayed(), 'Кнопка "Эконом класс" не отображается'

        business_btn = self.driver.find_element(By.CSS_SELECTOR, hp.BUSINESS_BTN)
        assert business_btn.is_displayed(), 'Кнопка "Бизнес класс" не отображается'

    def click_young_pax_btn(self):
        young_pax_btn = self.driver.find_element(By.CSS_SELECTOR, hp.YOUNG_PAX_BTN)
        young_pax_btn.click()

        class_attribute = young_pax_btn.get_attribute('class')
        assert 'text-white' in class_attribute, 'Кнопка "Молодежный" не выделена синим'

        number_of_tariffs = self.driver.find_elements(By.CSS_SELECTOR, hp.PASSENGERS_TITLE)
        assert len(number_of_tariffs) == 1, 'Количество тарифов не равняется одному'

        econom_btn = self.driver.find_element(By.CSS_SELECTOR, hp.ECONOM_BTN)
        assert econom_btn.is_displayed(), 'Кнопка "Эконом класс" не отображается'

        locator = (By.CSS_SELECTOR, hp.BUSINESS_BTN)
        wait = WebDriverWait(self.driver, 3)
        try:
            wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            assert False, 'Кнопка "Бизнес класс" отображается, но не должна'

    def choose_pax_class(self, pax_class):
        """На вход принимает название класса econom или business"""
        business_btn = self.driver.find_element(By.CSS_SELECTOR, hp.BUSINESS_BTN)
        econom_btn = self.driver.find_element(By.CSS_SELECTOR, hp.ECONOM_BTN)
        if pax_class == 'econom':
            econom_btn.click()
            class_attribute = econom_btn.get_attribute('class')
            assert "bg-blue-300" in class_attribute, 'Кнопка "Эконом класс" не выделена синим'
        elif pax_class == 'business':
            business_btn.click()
            class_attribute = business_btn.get_attribute('class')
            assert "bg-blue-300" in class_attribute, 'Кнопка "Бизнес класс" не выделена синим'

    def change_passengers_amount(self, pax_type, change, amount=1):
        """На вход принимает тип пакса, увеличение(+) или уменьшение(-), количество нажатий"""
        decrease_btn = self.driver.find_elements(By.CSS_SELECTOR, hp.DECREASE_BTN)
        increase_btn = self.driver.find_elements(By.CSS_SELECTOR, hp.INCREASE_BTN)
        if change == '-':
            for _ in range(amount):
                decrease_btn[pax_type].click()
        elif change == '+':
            for _ in range(amount):
                increase_btn[pax_type].click()

    def check_limits_of_amount_passengers(self, pax_types: list[str], disabled: str):
        """На вход принимает СПИСОК типов пакса, "+" или "-" для проверки отключения кнопки"""
        button_locator = hp.INCREASE_BTN if disabled == '+' else hp.DECREASE_BTN
        for pax_type in pax_types:
            self._check_pax_counter_button(pax_type, disabled, button_locator)

    def _check_pax_counter_button(self, pax_type: str, disabled: str, button_locator: str):
        counter_button = self.driver.find_elements(By.CSS_SELECTOR, button_locator)

        pax_counter_button_enabled = not counter_button[pax_type].is_enabled()
        assert pax_counter_button_enabled, f'Кнопка {disabled} остается активной, но не должна'

    def check_adults_not_less_than_infant(self):
        counter = self.driver.find_elements(By.CSS_SELECTOR, hp.COUNTER)
        condition = int(counter[2].text) <= int(counter[0].text)
        assert condition, 'Младенцев не должно быть больше чем взрослых'

    def check_pax_summ_is_less_than_9(self):
        counter = self.driver.find_elements(By.CSS_SELECTOR, hp.COUNTER)
        pax_summ = sum(int(counter[i].text) for i in range(3))
        assert pax_summ <= 9, 'Количество пассажиров не должно превышать 9'

    def check_date_input(self):
        date_pick_button = self.driver.find_elements(By.CSS_SELECTOR, hp.DATE_PICK_BUTTON)
        text_date_pick_button = date_pick_button[0].text
        unexpected_text = 'Дата туда и обратно'
        condition = unexpected_text not in text_date_pick_button
        assert condition, 'Дата перелета не подставляется в кнопке'

    def click_date_pick_button(self, index=0):
        """На вход принимает цифровой индекс для случаев со сложным маршрутом"""
        date_pick_button = self.driver.find_elements(By.CSS_SELECTOR, hp.DATE_PICK_BUTTON)
        date_pick_button[index].click()

        if index == 0:
            tomorrow_date = self.driver.find_element(By.CSS_SELECTOR, hp.DAY_TOMORROW)
            bottom_state = tomorrow_date.get_attribute('class')
            assert 'hover:to-transparent' in bottom_state, ' Завтрашний день не выбран'

        first_month = self.driver.find_element(By.CSS_SELECTOR, hp.FIRST_MONTH_IN_LIST)
        assert first_month.is_displayed(), 'Кнопка первого месяца в списке не отображается'

        last_month = self.driver.find_element(By.CSS_SELECTOR, hp.LAST_MONTH_IN_LIST)
        assert last_month.is_displayed(), 'Кнопка последнего месяца в списке не отображается'

        to_date = self.driver.find_element(By.CSS_SELECTOR, hp.TO_DATE_INPUT)
        assert to_date.is_displayed(), 'Кнопка "Дата туда" не отображается'

        back_date = self.driver.find_element(By.CSS_SELECTOR, hp.BACK_DATE_INPUT)
        assert back_date.is_displayed(), 'Кнопка "Дата обратно" не отображается'

        not_back_date = self.driver.find_element(By.CSS_SELECTOR, hp.I_DONT_NEED_BACK)
        assert not_back_date.is_displayed(), 'Кнопка "Не нужен обратный билет" не отображается'

        prev_month = self.driver.find_element(By.CSS_SELECTOR, hp.PREV_MONTH_BUTTON)
        assert prev_month.is_displayed(), 'Кнопка "<" не отображается'

        next_month = self.driver.find_element(By.CSS_SELECTOR, hp.NEXT_MONTH_BUTTON)
        assert next_month.is_displayed(), 'Кнопка ">" не отображается'

    def check_upper_bound_dates(self):
        last_month = self.driver.find_element(By.CSS_SELECTOR, hp.LAST_MONTH_IN_LIST)
        last_month.click()

        last_month_attribute = last_month.get_attribute('class')
        assert '--active' in last_month_attribute, 'Выбранный месяц не становится активным'

        next_month = self.driver.find_element(By.CSS_SELECTOR, hp.NEXT_MONTH_BUTTON)
        assert not next_month.is_enabled(), 'Кнопка ">" остается активной, но не должна'

        day_361 = self.driver.find_element(By.CSS_SELECTOR, hp.DAY_361TH)
        assert not day_361.is_enabled(), 'Кнопка 361 дня остается активной, но не должна'

        day_360 = self.driver.find_element(By.CSS_SELECTOR, hp.DAY_360TH)
        assert day_360.is_enabled(), 'Кнопка 360 дня дизэйбл, но не должна'

    def check_lower_bound_dates(self):
        first_month = self.driver.find_element(By.CSS_SELECTOR, hp.FIRST_MONTH_IN_LIST)
        first_month.click()

        first_month_attribute = first_month.get_attribute('class')
        assert '--active' in first_month_attribute, 'Выбранный месяц не становится активным'

        prev_month = self.driver.find_element(By.CSS_SELECTOR, hp.PREV_MONTH_BUTTON)
        assert not prev_month.is_enabled(), 'Кнопка "<" остается активной, но не должна'

        day_yesterday = self.driver.find_element(By.CSS_SELECTOR, hp.DAY_YESTERDAY)
        assert not day_yesterday.is_enabled(), 'Кнопка вчера остается активной, но не должна'

        day_today = self.driver.find_element(By.CSS_SELECTOR, hp.DAY_TODAY)
        assert day_today.is_enabled(), 'Кнопка текщего дня дизэйбл, но не должна'

    def set_date_value(self, key):
        data = {
            'departure': {'direction_element': hp.TO_DATE_INPUT, 'day_element': hp.DAY_TODAY},
            'return': {'direction_element': hp.BACK_DATE_INPUT, 'day_element': hp.DAY_15TH},
        }
        date_data = data[key]
        choose_to_date = self.driver.find_element(By.CSS_SELECTOR, date_data['direction_element'])
        choose_to_date.click()
        choose_dep_day = self.driver.find_element(By.CSS_SELECTOR, date_data['day_element'])
        choose_dep_day.click()
        flights = self.driver.find_elements(By.CSS_SELECTOR, hp.DATE_PICK_BUTTON)
        if len(flights) == 1:
            bottom_state = choose_dep_day.get_attribute('class')
            assert 'hover:to-transparent' in bottom_state, 'Выбранный день не выделен'

    def set_i_dont_need_back(self):
        choose_dont_need_back = self.driver.find_element(By.CSS_SELECTOR, hp.I_DONT_NEED_BACK)
        choose_dont_need_back.click()

        locator = (By.XPATH, hp.CALENDAR_WINDIW)
        wait = WebDriverWait(self.driver, 1)
        try:
            wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            assert False, 'Кнопка "Мне не нужен билет обратно" отображается, но не должна'
