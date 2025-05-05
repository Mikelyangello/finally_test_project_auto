from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import pytest


def link_compilator(excluded_link=None, number_of_links=10):
    base = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    return [base + str(i) if i != excluded_link else pytest.param(base + str(i), marks=pytest.mark.xfail)
            for i in range(number_of_links)]


@pytest.mark.parametrize('link', link_compilator(7))
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_item_to_basket_notification()
    page.should_be_correct_price_of_product()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, mc):
    page = ProductPage(browser, mc.def_link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser, mc):
    page = ProductPage(browser, mc.def_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, mc):
    page = ProductPage(browser, mc.def_link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_url()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, mc):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link, mc=mc)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url, mc=mc)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()
