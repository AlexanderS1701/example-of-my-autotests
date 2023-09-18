import allure
import pytest


@pytest.mark.regression
@allure.title('Просмотр главной страницы для нового пользователя')
@allure.label('testcase', '6205')
def test_main_page_first_scan(app):
    app.home_page.check_header()
    app.home_page.check_placeholders()
    app.home_page.check_swap_city_button()
    app.home_page.check_passengers_data_input()
    app.home_page.check_text_content_in_passengers_button()
    app.home_page.check_complex_route_button()
    app.home_page.check_hotel_checkbox()
    app.home_page.check_search_button()
    app.home_page.check_search_history_is_missing()


@pytest.mark.regression
@pytest.mark.parametrize('dep_city , arr_city', [
    ({'code': 'NQZ', 'name': 'Аст'}, {'code': 'ALA', 'name': 'Алм'})
])
@allure.title('Повторный просмотр главной страницы после ввода данных без поиска')
@allure.label('testcase', '6206')
def test_main_page_scan_without_search(app, dep_city, arr_city):
    app.home_page.select_departure(dep_city['name'])
    app.home_page.select_arrival(arr_city['name'])
    app.home_page.click_date_pick_button()
    app.home_page.set_date_value('departure')
    app.home_page.set_date_value('return')
    app.driver.refresh()
    app.home_page.check_placeholders()
    app.home_page.check_passengers_data_input()
    app.home_page.check_search_history_is_missing()


@pytest.mark.regression
@pytest.mark.parametrize('dep_city , arr_city', [
    ({'code': 'NQZ', 'name': 'Аст'}, {'code': 'ALA', 'name': 'Алм'})
])
@allure.title('Просмотр главной страницы после поиска')
@allure.label('testcase', '6207')
def test_main_page_scan_with_search(app, dep_city, arr_city):
    app.home_page.select_departure(dep_city['name'])
    app.home_page.select_arrival(arr_city['name'])
    app.home_page.click_date_pick_button()
    app.home_page.set_date_value('departure')
    app.home_page.set_i_dont_need_back()
    app.home_page.click_search_button()
    app.ticket_page.wait_search_end()
    app.ticket_page.click_on_avia_button()
    app.home_page.check_city('departure', dep_city['name'])
    app.home_page.check_city('arrival', arr_city['name'])
    app.home_page.check_date_input()
    app.home_page.check_search_history()


@pytest.mark.regression
@pytest.mark.parametrize('dep_city , arr_city', [
    ({'code': 'NQZ', 'name': 'Аст'}, {'code': 'ALA', 'name': 'Алм'})
])
@allure.title('Переключение между городами (Switch Cities)')
@allure.label('testcase', '6211')
def test_main_page_swap_cities(app, dep_city, arr_city):
    app.home_page.select_departure(dep_city['name'])
    app.home_page.select_arrival(arr_city['name'])
    app.home_page.click_swap_button()
    app.home_page.check_city('departure', arr_city['name'])
    app.home_page.check_city('arrival', dep_city['name'])


@pytest.mark.regression
@pytest.mark.parametrize('dep_city , arr_city', [
    ({'code': 'NQZ', 'name': 'Аст'}, {'code': 'ALA', 'name': 'Алм'})
])
@allure.title('Ввод данных через историю поисковых запросов')
@allure.label('testcase', '6243')
def test_main_page_enter_search_history(app, dep_city, arr_city):
    app.home_page.select_departure(dep_city['name'])
    app.home_page.select_arrival(arr_city['name'])
    app.home_page.click_date_pick_button()
    app.home_page.set_date_value('departure')
    app.home_page.set_i_dont_need_back()
    app.home_page.click_search_button()
    app.ticket_page.wait_search_end()
    app.ticket_page.click_on_avia_button()
    app.home_page.click_swap_button()
    app.home_page.click_history_1_button()
    app.home_page.check_city('departure', dep_city['name'])
    app.home_page.check_city('arrival', arr_city['name'])


@pytest.mark.regression
@allure.title('Составление сложного маршрута с более,чем 4 (максимальное значение) перелетами и их удаление')
@allure.label('testcase', '6221')
def test_main_page_max_4_complex_route(app):
    app.home_page.click_complex_route_button()
    app.home_page.check_remove_complex_route_button()
    app.home_page.click_complex_route_button()
    app.home_page.click_complex_route_button()
    app.home_page.check_complex_route_button()
    app.home_page.click_remove_complex_route_button(2)
    app.home_page.check_complex_route_button()
    app.home_page.click_remove_complex_route_button(1)
    app.home_page.click_remove_complex_route_button(0)


@pytest.mark.regression
@pytest.mark.parametrize('city_1 , city_2, city_3', [
    ({'code': 'ALA', 'name': 'Алм'},
     {'code': 'NQZ', 'name': 'Аст'},
     {'code': 'CIT', 'name': 'Шым'})
])
@allure.title('Составление сложного маршрута с последующим поиском')
@allure.label('testcase', '6224')
def test_main_page_search_with_complex_route(app, city_1, city_2, city_3):
    app.home_page.click_complex_route_button()
    app.home_page.select_departure(city_1['name'], 0)
    app.home_page.select_arrival(city_2['name'], 0)
    app.home_page.click_date_pick_button()
    app.home_page.set_date_value('departure')
    app.home_page.select_departure(city_2['name'], 1)
    app.home_page.select_arrival(city_3['name'], 1)
    app.home_page.click_date_pick_button(1)
    app.home_page.set_date_value('return')
    app.home_page.click_search_button()
    app.ticket_page.wait_search_end()
    app.ticket_page.check_ticket_list()


@pytest.mark.regression
@allure.title('Просмотр отображения элементов окна для выбора класса и количества пассажиров')
@allure.label('testcase', '6225')
def test_main_page_elements_display_in_the_passenger_input_window(app):
    app.home_page.click_passengers_data_input()
    app.home_page.click_young_pax_btn()
    app.home_page.click_default_pax_btn()
    app.home_page.choose_pax_class('business')
    app.home_page.choose_pax_class('econom')


@pytest.mark.regression
@pytest.mark.parametrize('pax', [
    {'adult_id': 0, 'child_id': 1, 'infant_id': 2}
])
@allure.title('Проверка ограничений на добавление пассажиров (максимум 9, минимум 1)')
@allure.label('testcase', '6226')
def test_main_page_limit_of_amount_passengers(app, pax):
    app.home_page.click_passengers_data_input()
    app.home_page.check_limits_of_amount_passengers(list(pax.values()), disabled='-')
    app.home_page.change_passengers_amount(pax['adult_id'], change='+', amount=9)
    app.home_page.check_pax_summ_is_less_than_9()
    app.home_page.check_limits_of_amount_passengers(list(pax.values()), disabled='+')
    app.home_page.change_passengers_amount(pax['adult_id'], change='-', amount=8)
    app.home_page.check_limits_of_amount_passengers(list(pax.values()), disabled='-')
    app.home_page.change_passengers_amount(pax['child_id'], change='+', amount=8)
    app.home_page.check_limits_of_amount_passengers(list(pax.values()), disabled='+')
    app.home_page.change_passengers_amount(pax['child_id'], change='-', amount=8)
    app.home_page.change_passengers_amount(pax['adult_id'], change='+', amount=4)
    app.home_page.change_passengers_amount(pax['infant_id'], change='+', amount=4)
    app.home_page.check_limits_of_amount_passengers(list(pax.values()), disabled='+')


@pytest.mark.regression
@pytest.mark.parametrize('pax', [
    {'adult_id': 0, 'child_id': 1, 'infant_id': 2}
])
@allure.title('Проверка обязательности взрослого пассажира на каждого младенца')
@allure.label('testcase', '6227')
def test_main_page_min_one_adult_for_one_infant(app, pax):
    app.home_page.click_passengers_data_input()
    app.home_page.change_passengers_amount(pax['adult_id'], change='+', amount=2)
    app.home_page.change_passengers_amount(pax['infant_id'], change='+', amount=3)
    app.home_page.check_limits_of_amount_passengers([pax['infant_id']], disabled='+')
    app.home_page.change_passengers_amount(pax['adult_id'], change='-', amount=2)
    app.home_page.check_limits_of_amount_passengers([pax['infant_id']], disabled='+')
    app.home_page.check_adults_not_less_than_infant()


@pytest.mark.regression
@pytest.mark.parametrize('pax', [
    {'adult_id': 0, 'child_id': 1, 'infant_id': 2}
])
@allure.title('Проверка отображения изменения пассажиров в плейсхолдере кнопки')
@allure.label('testcase', '6229')
def test_main_page_text_content_in_passengers_button(app, pax):
    app.home_page.click_passengers_data_input()
    app.home_page.choose_pax_class('business')
    app.home_page.change_passengers_amount(pax['adult_id'], change='+', amount=2)
    app.home_page.change_passengers_amount(pax['child_id'], change='+', amount=2)
    app.home_page.change_passengers_amount(pax['infant_id'], change='+', amount=2)
    app.home_page.check_text_content_in_passengers_button(
        pax_class='Бизнес', amount='3 взр, 2 дет, 2 мл'
    )


@pytest.mark.regression
@allure.title('Проверка работы валидации дат в календаре')
@allure.label('testcase', '6236')
def test_main_page_scan_to_calendar(app):
    app.home_page.click_date_pick_button()
    app.home_page.check_upper_bound_dates()
    app.home_page.check_lower_bound_dates()
